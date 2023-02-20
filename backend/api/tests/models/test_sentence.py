# -*- coding: utf-8 -*-
"""Module for testing Sentence model"""
from datetime import timedelta
from pathlib import Path

from analyst_report_summarizer.settings import DATETIME_TEST_LEEWAY, TEST_RESOURCES_ROOT
from api.grobid_tfidf_code.main import split_into_sentences
from api.models.report import Report
from api.models.sentence import Sentence
from django.test import TestCase
from django.utils import timezone


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

    plaintext_sentences = split_into_sentences(plaintext)

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
        sample_sentence_text = "Sample Sentence Text"
        sample_tfidf_weight = 1.0

        report = self._load_test_report()
        sentence = Sentence.objects.create(
            report, sample_sentence_text, sample_tfidf_weight
        )

        report_sentences = report.sentences.all()
        self.assertIn(sentence, report_sentences)
        self.assertEqual(1, len(report_sentences))

        self.assertEqual(sentence.text, sample_sentence_text)
        self.assertEqual(sentence.tf_idf_weight, sample_tfidf_weight)

    def test_sentence_extraction_from_report(self):
        """Test to see that the correct sentences are extracted
        from the report plaintext as specified in the function split_into_sentences()"""
        report = self._load_test_report()
        sentences = Sentence.objects.extract_sentences(report)
        self.assertEqual(
            len(sentences),
            len(self.plaintext_sentences),
            msg="number of sentence objects aren't the same as the expected number",
        )

        for sentence in sentences:
            self.assertIn(sentence.text, self.plaintext_sentences)
        report.delete()

    def test_deletion_with_report(self):
        """Test to see if a Sentence is deleted with it's associated report"""
        report = self._load_test_report()
        sentences = Sentence.objects.extract_sentences(report)
        num_sentences = len(sentences)

        sentence_count = Sentence.objects.all().count()

        deleted, _ = report.delete()
        self.assertGreater(deleted, 1)
        self.assertEqual(
            sentence_count - num_sentences,
            Sentence.objects.filter(parent_report=report).count(),
        )

    def test_tfidf_weight(self):
        """Test to see if the tfidf weight calculated for a sentence is correct"""
        # Currently not implemented as too time-consuming

    def test_sentence_extraction_time(self):
        """Test to see if the sentence extraction time is correctly set in a parent report"""
        now = timezone.now()
        report = self._load_test_report()
        Sentence.objects.extract_sentences(report)

        self.assertIsNotNone(report.sentence_datetime)
        self.assertGreater(
            report.sentence_datetime, now - timedelta(seconds=DATETIME_TEST_LEEWAY)
        )
        self.assertLess(
            report.sentence_datetime, now + timedelta(seconds=DATETIME_TEST_LEEWAY)
        )
