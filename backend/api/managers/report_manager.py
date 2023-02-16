# -*- coding: utf-8 -*-
"""Module for ReportManager"""
from analyst_report_summarizer.settings import GROBID_CONFIG
from api.grobid_client.grobid_client import GrobidClient
from django.core.files import File
from django.db.models.manager import Manager


class ReportManager(Manager):  # pylint: disable=too-few-public-methods
    """Manager for creation of Report objects"""

    def create(
        self, report_file: File, *args, **kwargs
    ):  # pylint: disable=unused-argument
        """Method to create a Report model from the file pdf

        This will involve calling the grobid server configured in settings to extract the TEI XML"""
        client: GrobidClient = GrobidClient(config_dict=GROBID_CONFIG)
        _, _, tei_xml = client.process_pdf(
            "processFulltextDocument",
            report_file.name,
            pdf_bytes=report_file.open("rb"),
        )
        return super().create(*args, tei_xml=tei_xml, **kwargs)
