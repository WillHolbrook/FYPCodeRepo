# -*- coding: utf-8 -*-
"""Module for testing Report model"""
import xml.etree.ElementTree as ET
from datetime import timedelta
from pathlib import Path

from analyst_report_summarizer.settings import TEST_RESOURCES_ROOT
from api.grobid_tfidf_code.main import extract_text_from_element_tree
from api.models.report import Report
from django.contrib.auth import get_user_model
from django.core.files import File
from django.test import TestCase
from django.utils import timezone


class ReportTestCase(TestCase):
    """Tests for Report Model

    Note this doesn't test the API endpoints that cause updates to this model
    """

    @staticmethod
    def _load_test_pdf(
        path: Path = TEST_RESOURCES_ROOT.joinpath(Path("test.pdf")),
    ) -> File:
        """Method to load the test pdf used across multiple tests"""
        return File(open(path, "rb"), path.name)

    def test_report_creation(self):
        """Test to see if a Report can be created"""
        number_of_reports = Report.objects.count()
        Report.objects.create(self._load_test_pdf())
        self.assertEqual(
            Report.objects.count(),
            number_of_reports + 1,
            msg="Profile not automatically created",
        )

    def test_tei_xml_extraction(self):
        """Test to see if correct tei_xml can be extracted from a file"""
        report = Report.objects.create(self._load_test_pdf())

        with open(
            TEST_RESOURCES_ROOT.joinpath(Path("test.tei.xml")), encoding="utf-8"
        ) as file:
            expected_text = extract_text_from_element_tree(ET.fromstring(file.read()))

        test_text = extract_text_from_element_tree(ET.fromstring(report.tei_xml))

        self.assertEqual(
            test_text, expected_text, msg="The extracted tei.xml isn't as expected"
        )

    def test_upload_with_user_set(self):
        """Test to see if report can be created with user link"""
        created_user = get_user_model().objects.create_user("user2", "password")
        self._create_two_reports_for_user(created_user)
        created_user.delete()

    def test_upload_without_user_set(self):
        """Test to see if report can be created without user link"""
        report = Report.objects.create(self._load_test_pdf())

        self.assertIsNone(report.user)

    def _create_two_reports_for_user(self, user: get_user_model()) -> [Report, Report]:
        """
        Helper method to create two reports for the given user
        and check to see the reports are created and linked correctly

        Args:
            user: the user to create the reports for

        Returns:
            A tuple of the two created reports
        """
        report1 = Report.objects.create(self._load_test_pdf(), user=user)
        report2 = Report.objects.create(self._load_test_pdf(), user=user)

        reports = user.reports.all()

        self.assertIn(report1, reports)
        self.assertIn(report2, reports)
        return report1, report2

    def test_deletion_with_user(self):
        """Test to see if report associated with a user is deleted"""
        created_user = get_user_model().objects.create_user("user3", "password")
        self._create_two_reports_for_user(created_user)

        number_of_reports = Report.objects.count()
        created_user.delete()
        self.assertEqual(
            Report.objects.count(),
            number_of_reports - 2,
            msg="The 2 reports were not deleted when the user was deleted",
        )
        self.assertEqual(len(Report.objects.filter(user=created_user)), 0)

    def test_upload_time(self):
        """Test to see if the upload time is set correctly with a 10 second margin of error"""
        now = timezone.now()
        report = Report.objects.create(self._load_test_pdf())

        self.assertGreater(report.upload_datetime, now - timedelta(seconds=10))
        self.assertLess(report.upload_datetime, now + timedelta(seconds=10))
