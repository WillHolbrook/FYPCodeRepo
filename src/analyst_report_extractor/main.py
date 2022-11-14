from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree
import re

from pathlib import Path


# TODO add a return value probably a list of paths of outputted files
def extract_tei_xml_from_pdf(input_folder_filepath: Path, output_folder_filepath: Path,
                             grobid_client: GrobidClient) -> None:
    """
    Extracts .tei.xml files from .pdf files using a setup grobid server

    Args:
        input_folder_filepath: path to the folder containing the PDFs to process
        output_folder_filepath: path to the folder to output PDFs to
        grobid_client: a GrobidClient instance connected to a valid client

    Returns:
        None
    """
    grobid_client.process("processFulltextDocument", input_folder_filepath, output=output_folder_filepath, n=20)


# TODO add a return value maybe a success code or length of string extracted?
def extract_text_from_xml(input_filepath: Path, output_filepath: Path, write_mode: str = "w") -> None:
    """
    Extracts text from .tei.xml files only retaining 1 newline between text

    Args:
        input_filepath: path to the .tei.xml file to extract files from e.g. Path("../resources/output_tei_xml/file.tei.xml")
        output_filepath: path to output the file to e.g. Path("../resources/output_txt/file.txt")
        write_mode:

    Returns:

    """
    tree = ET.parse(input_filepath)
    root: Element = tree.getroot()
    text: str = "".join(root.itertext())
    text = re.sub(r"\s*?(\n)\s*", "\n", text)

    with open(output_filepath, write_mode, encoding="utf-8") as f:
        f.write(text)


def main():
    # TODO add some handling around the grobid server being down

    client: GrobidClient = GrobidClient(config_path="./grobid_config.json")
    input_folder_path = Path("../resources/input_pdfs")
    tei_xml_output_folder_path = Path("../resources/output_tei_xml")
    extract_tei_xml_from_pdf(input_folder_path, tei_xml_output_folder_path, client)

    txt_output_folder_path = Path("../resources/output_txt")
    for filepath in tei_xml_output_folder_path.rglob("*.tei.xml"):
        extract_text_from_xml(filepath, txt_output_folder_path.joinpath(f"./{filepath.name}.txt"))


if __name__ == "__main__":
    main()
