# -*- coding: utf-8 -*-
# pylint: disable=[fixme,redundant-unittest-assert]
"""Module for testing Report model"""
from pathlib import Path

from analyst_report_summarizer.settings import TEST_RESOURCES_ROOT
from api.models.report import Report
from django.core.files import File
from django.test import TestCase


class ReportTestCase(TestCase):
    """Tests for Report Model

    Note this doesn't test the API endpoints that cause updates to this model
    """

    @staticmethod
    def _load_test_pdf(
        path: Path = TEST_RESOURCES_ROOT.joinpath(Path("test.pdf")),
    ) -> File:
        with open(path, "rb") as file:
            return File(file, path.name)

    def test_report_creation(self):
        """Test to see if a Report can be created"""
        Report.objects.create(self._load_test_pdf())

    def test_tei_xml_extraction(self):
        """Test to see if correct tei_xml can be extracted from a file"""
        report = Report.objects.create(  # pylint: disable=unused-variable
            self._load_test_pdf()
        )

    # TODO
    def test_upload_with_user_set(self):
        """Test to see if report can be created with user link"""
        self.assertTrue(False)

    # TODO
    def test_upload_without_user_set(self):
        """Test to see if report can be created without user link"""
        self.assertTrue(False)

    # TODO
    def test_deletion_with_user(self):
        """Test to see if report associated with a user is deleted"""
        self.assertTrue(False)
