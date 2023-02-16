# -*- coding: utf-8 -*-
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from xml.etree.ElementTree import Element

from analyst_report_summarizer.settings import GROBID_CONFIG
from api.grobid_client.grobid_client import GrobidClient


# TODO add a return value probably a list of paths of outputted files
def extract_tei_xml_from_pdf(
    input_folder_filepath: Path,
    output_folder_filepath: Path,
    grobid_client: GrobidClient,
) -> None:
    """
    Extracts .tei.xml files from .pdf files using a setup grobid server

    Args:
        input_folder_filepath: path to the folder containing the PDFs to process
        output_folder_filepath: path to the folder to output PDFs to
        grobid_client: a GrobidClient instance connected to a valid client

    Returns:
        None
    """
    grobid_client.process(
        "processFulltextDocument",
        input_folder_filepath,
        output=output_folder_filepath,
        n=20,
    )


# TODO add a return value maybe a success code or length of string extracted?
def extract_text_from_xml_file(
    input_filepath: Path, output_filepath: Path, write_mode: str = "w"
) -> None:
    """
    Extracts text from .tei.xml files only retaining 1 newline between text

    Args:
        input_filepath: path to the .tei.xml file to extract files from e.g. Path("../resources/output_tei_xml/file.tei.xml")
        output_filepath: path to output the file to e.g. Path("../resources/output_txt/file.txt")
        write_mode:

    Returns:

    """
    tree = ET.parse(input_filepath)
    text = extract_text_from_element_tree(tree.getroot())

    with open(output_filepath, write_mode, encoding="utf-8") as f:
        f.write(text)


def extract_text_from_element_tree(root: ET.Element) -> str:
    text: str = "".join(root.itertext())
    return re.sub(r"\s*?(\n)\s*", "\n", text)


def print_datetime_name_and_paths_tab_separated(root_folder_path: Path):
    for input_folder_path in root_folder_path.rglob("*.pdf"):
        datetime_str = re.sub(r"(\d+)_.*", r"\1", input_folder_path.name)
        datetime_obj = datetime.strptime(datetime_str, "%Y%m%d")
        print(f"{input_folder_path}\t{input_folder_path.name}\t{datetime_obj}")


# TODO add some handling around the grobid server being down
def extract_tei_xml_from_root(
    root_output_folder_path: Path,
    root_input_folder_path: Path,
    grobid_client: GrobidClient,
) -> None:
    if not root_output_folder_path.exists():
        root_output_folder_path.mkdir()

    for input_folder_path in root_input_folder_path.glob("*"):
        if input_folder_path.is_dir():
            tei_xml_output_folder_path = root_output_folder_path.joinpath(
                f"./{input_folder_path.name}"
            )
            if not tei_xml_output_folder_path.is_dir():
                tei_xml_output_folder_path.mkdir()
            print(input_folder_path, tei_xml_output_folder_path)

            extract_tei_xml_from_pdf(
                input_folder_path, tei_xml_output_folder_path, grobid_client
            )


def extract_txt_from_root(root_output_folder_path: Path, root_input_folder_path: Path):
    for input_folder_path in root_output_folder_path.glob("*"):
        if input_folder_path.is_dir():
            txt_output_folder_path = root_input_folder_path.joinpath(
                f"./{input_folder_path.name}"
            )
            if not txt_output_folder_path.is_dir():
                txt_output_folder_path.mkdir()
            print(f"Extracting from folder {txt_output_folder_path}")

            for filepath in input_folder_path.rglob("*.tei.xml"):
                extract_text_from_xml_file(
                    filepath, txt_output_folder_path.joinpath(f"./{filepath.name}.txt")
                )


def get_sub_file_count(root_folder_path: Path) -> int:
    count = 0

    for file in root_folder_path.rglob("*"):
        if file.is_file():
            count += 1

    return count


def main():
    client: GrobidClient = GrobidClient(config_dict=GROBID_CONFIG)
    root_folder_path = Path("./api/tests/resources").resolve()
    root_tei_xml_output_folder_path = Path("./api/tests/resources").resolve()
    # root_txt_output_folder_path = Path(
    #     "../../FilestoreRepo/FTSE100Info/txtReports"
    # ).resolve()

    count = get_sub_file_count(root_folder_path)
    print(f"Number of Reports: {count}")
    # print_datetime_name_and_paths_tab_separated(root_folder_path)

    extract_tei_xml_from_pdf(root_folder_path, root_folder_path, client)
    # extract_tei_xml_from_root(root_tei_xml_output_folder_path, root_folder_path, client)
    # extract_txt_from_root(root_txt_output_folder_path, root_tei_xml_output_folder_path)


if __name__ == "__main__":
    main()
