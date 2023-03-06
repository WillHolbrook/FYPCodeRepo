# -*- coding: utf-8 -*-
# pylint: skip-file
"""

Grobid Python Client

This version uses the standard ThreadPoolExecutor for parallelizing the
concurrent calls to the GROBID services.  Given the limits of
ThreadPoolExecutor (input stored in memory, blocking Executor.map until the
whole input is acquired), it works with batches of PDF of a size indicated
in the config.json file (default is 1000 entries). We are moving from first
batch to the second one only when the first is entirely processed - which
means it is slightly sub-optimal, but should scale better. Working without
batch would mean acquiring a list of millions of files in directories and
would require something scalable too (e.g. done in a separate thread),
which is not implemented for the moment.

"""
import argparse
import concurrent.futures
import io
import json
import ntpath
import os
import pathlib
import time

import requests

from .client import ApiClient


class ServerUnavailableException(Exception):
    pass


def _output_file_name(input_file, input_path, output):
    # we use ntpath here to be sure it will work on Windows too
    if output is not None:
        input_file_name = str(os.path.relpath(os.path.abspath(input_file), input_path))
        filename = os.path.join(
            output, os.path.splitext(input_file_name)[0] + ".tei.xml"
        )
    else:
        input_file_name = ntpath.basename(input_file)
        filename = os.path.join(
            ntpath.dirname(input_file),
            os.path.splitext(input_file_name)[0] + ".tei.xml",
        )

    return filename


class GrobidClient(ApiClient):
    def __init__(
        self,
        grobid_server="localhost",
        batch_size=1000,
        coordinates=None,
        sleep_time=5,
        timeout=60,
        config_path=None,
        check_server=True,
        config_dict=None,
    ):

        if coordinates is None:
            coordinates = ["persName", "figure", "ref", "biblStruct", "formula", "s"]

        if config_path:
            self._load_config(config_path)
        elif config_dict:
            self.config = config_dict
        else:
            self.config = {
                "grobid_server": grobid_server,
                "batch_size": batch_size,
                "coordinates": coordinates,
                "sleep_time": sleep_time,
                "timeout": timeout,
            }
        if check_server:
            self._test_server_connection()

    def _load_config(self, path="./config.json"):
        """
        Load the json configuration
        """
        config_json = open(path).read()
        self.config = json.loads(config_json)

    def _test_server_connection(self):
        """Test if the server is up and running."""
        the_url = self.config["grobid_server"] + "/api/isalive"
        try:
            r = requests.get(the_url)
        except:
            print(
                "GROBID server does not appear up and running, the connection to the server failed"
            )
            raise ServerUnavailableException()

        status = r.status_code

        if status != 200:
            raise ServerUnavailableException(
                "GROBID server does not appear up and running " + str(status)
            )

    def process(
        self,
        service,
        input_path,
        output=None,
        n=10,
        generateIDs=False,
        consolidate_header=True,
        consolidate_citations=False,
        include_raw_citations=False,
        include_raw_affiliations=False,
        tei_coordinates=False,
        segment_sentences=False,
        force=True,
        verbose=False,
    ):
        batch_size_pdf = self.config["batch_size"]
        input_files = []

        for (dirpath, dirnames, filenames) in os.walk(input_path):
            for filename in filenames:
                if (
                    filename.endswith(".pdf")
                    or filename.endswith(".PDF")
                    or (
                        service == "processCitationList"
                        and (filename.endswith(".txt") or filename.endswith(".TXT"))
                    )
                ):
                    if verbose:
                        try:
                            print(filename)
                        except Exception:
                            # may happen on linux see https://stackoverflow.com/questions/27366479/python-3-os-walk-file-paths-unicodeencodeerror-utf-8-codec-cant-encode-s
                            pass
                    input_files.append(os.sep.join([dirpath, filename]))

                    if len(input_files) == batch_size_pdf:
                        self.process_batch(
                            service,
                            input_files,
                            input_path,
                            output,
                            n,
                            generateIDs,
                            consolidate_header,
                            consolidate_citations,
                            include_raw_citations,
                            include_raw_affiliations,
                            tei_coordinates,
                            segment_sentences,
                            force,
                            verbose,
                        )
                        input_files = []

        # last batch
        if len(input_files) > 0:
            self.process_batch(
                service,
                input_files,
                input_path,
                output,
                n,
                generateIDs,
                consolidate_header,
                consolidate_citations,
                include_raw_citations,
                include_raw_affiliations,
                tei_coordinates,
                segment_sentences,
                force,
                verbose,
            )

    def process_batch(
        self,
        service,
        input_files,
        input_path,
        output,
        n,
        generateIDs,
        consolidate_header,
        consolidate_citations,
        include_raw_citations,
        include_raw_affiliations,
        tei_coordinates,
        segment_sentences,
        force,
        verbose=False,
    ):
        if verbose:
            print(len(input_files), "files to process in current batch")

        # we use ThreadPoolExecutor and not ProcessPoolExecutor because it is an I/O intensive process
        with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
            # with concurrent.futures.ProcessPoolExecutor(max_workers=n) as executor:
            results = []
            for input_file in input_files:
                # check if TEI file is already produced
                filename = _output_file_name(input_file, input_path, output)
                if not force and os.path.isfile(filename):
                    print(
                        filename,
                        "already exist, skipping... (use --force to reprocess pdf input files)",
                    )
                    continue

                selected_process = self.process_pdf
                if service == "processCitationList":
                    selected_process = self.process_txt

                r = executor.submit(
                    selected_process,
                    service,
                    input_file,
                    generateIDs,
                    consolidate_header,
                    consolidate_citations,
                    include_raw_citations,
                    include_raw_affiliations,
                    tei_coordinates,
                    segment_sentences,
                )

                results.append(r)

        for r in concurrent.futures.as_completed(results):
            input_file, status, text = r.result()
            filename = _output_file_name(input_file, input_path, output)

            if status != 200 or text is None:
                print(
                    "Processing of",
                    input_file,
                    "failed with error",
                    str(status),
                    ",",
                    text,
                )
                # writing error file with suffixed error code
                try:
                    pathlib.Path(os.path.dirname(filename)).mkdir(
                        parents=True, exist_ok=True
                    )
                    with open(
                        filename.replace(".tei.xml", "_" + str(status) + ".txt"),
                        "w",
                        encoding="utf8",
                    ) as tei_file:
                        if text is not None:
                            tei_file.write(text)
                        else:
                            tei_file.write("")
                except OSError:
                    print("Writing resulting TEI XML file", filename, "failed")
            else:
                # writing TEI file
                try:
                    pathlib.Path(os.path.dirname(filename)).mkdir(
                        parents=True, exist_ok=True
                    )
                    with open(filename, "w", encoding="utf8") as tei_file:
                        tei_file.write(text)
                except OSError:
                    print("Writing resulting TEI XML file", filename, "failed")

    def process_pdf(
        self,
        service,
        pdf_file_path,
        generate_ids=False,
        consolidate_header=True,
        consolidate_citations=False,
        include_raw_citations=False,
        include_raw_affiliations=False,
        tei_coordinates=False,
        segment_sentences=False,
        pdf_bytes=None,
    ):
        loaded_from_path = pdf_bytes is None
        if loaded_from_path:
            pdf_bytes = open(pdf_file_path, "rb")
        files = {
            "input": (
                pdf_file_path,
                pdf_bytes,
                "application/pdf",
                {"Expires": "0"},
            )
        }

        the_url = self.config["grobid_server"] + "/api/" + service

        # set the GROBID parameters
        the_data = {}
        if generate_ids:
            the_data["generateIDs"] = "1"
        if consolidate_header:
            the_data["consolidateHeader"] = "1"
        if consolidate_citations:
            the_data["consolidateCitations"] = "1"
        if include_raw_citations:
            the_data["includeRawCitations"] = "1"
        if include_raw_affiliations:
            the_data["includeRawAffiliations"] = "1"
        if tei_coordinates:
            the_data["teiCoordinates"] = self.config["coordinates"]
        if segment_sentences:
            the_data["segmentSentences"] = "1"

        try:
            res, status = self.post(
                url=the_url,
                files=files,
                data=the_data,
                headers={"Accept": "text/plain"},
                timeout=self.config["timeout"],
            )

            if status == 503:
                time.sleep(self.config["sleep_time"])
                return self.process_pdf(
                    service,
                    pdf_file_path,
                    generate_ids,
                    consolidate_header,
                    consolidate_citations,
                    include_raw_citations,
                    include_raw_affiliations,
                    tei_coordinates,
                    segment_sentences,
                )
        except requests.exceptions.ReadTimeout:
            if loaded_from_path:
                pdf_bytes.close()
            return pdf_file_path, 408, None
        if loaded_from_path:
            pdf_bytes.close()
        return pdf_file_path, status, res.text
