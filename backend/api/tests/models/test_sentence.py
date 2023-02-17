# -*- coding: utf-8 -*-
"""Module for testing Sentence model"""
from pathlib import Path

from analyst_report_summarizer.settings import TEST_RESOURCES_ROOT
from api.models.report import Report
from django.test import TestCase


class SentenceTestCase(TestCase):
    """Tests for the Sentence model
    Tests are decoupled from the Report and GROBID
    server by using create_without_file() to create report instances"""

    with open(
        TEST_RESOURCES_ROOT.joinpath(Path("test.plaintext")), "r", encoding="utf-8"
    ) as file:
        plaintext = file.read()

    with open(
        TEST_RESOURCES_ROOT.joinpath(Path("test.tei.xml")), "r", encoding="utf-8"
    ) as file:
        tei_xml = file.read()

    @staticmethod
    def _load_test_report() -> Report:
        """
        Method to create a report model instance from the preloaded
        plaintext and tei_xml members

        This uses create_without_file() meaning extraction is never
        done by the server

        Returns:
            A report with the default plaintext and tei_xml
        """
        return Report.objects._create_without_file(  # pylint: disable=protected-access
            tei_xml=SentenceTestCase.tei_xml, plaintext=SentenceTestCase.plaintext
        )

    def test_sentence_creation(self):
        """Test to see if a Sentence can be created
        with a given report object"""
        self.assertTrue(False)

    def test_sentence_extraction_from_report(self):
        """Test to see that the correct sentences are extracted
        from the report plaintext as specified in the function split_into_sentences()"""
        self.assertTrue(False)

    def test_deletion_with_report(self):
        """Test to see if a Sentence is deleted with it's associated report"""
        self.assertTrue(False)

    def test_tfidf_weight(self):
        """Test to see if the tfidf weight calculated for a sentence is correct"""
        # Currently not implemented as too time-consuming
        self.assertTrue(False)

    def test_sentence_extraction_time(self):
        """Test to see if the sentence extraction time is correctly set in a parent report"""
        self.assertTrue(False)
