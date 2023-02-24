# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
"""Module to test Report Upload API"""
from api.models.report import Report
from api.tests.models.test_report import ReportTestCase
from django.contrib.auth import get_user_model
from django.core.files import File
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestReportUpload(APITestCase):
    """Test Report Upload API"""

    fixtures = ["user_fixtures.json", "report_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_user_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_singular_report(self):
        """Test for uploading a report"""
        test_pdf: File = ReportTestCase.load_test_pdf()
        response = self.client.post(
            reverse("report_upload"), {"uploaded_report": test_pdf}
        )

        report = Report.objects.create(test_pdf)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        report_data = response.data

        self.assertEqual(report_data["tei_xml"], report.tei_xml)
        self.assertEqual(report_data["plaintext"], report.plaintext)

    def test_bad_request(self):
        """Test for calling the upload endpoint without a valid file"""
        response = self.client.post(reverse("report_upload"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_non_logged_in_user(self):
        """Test for uploading a report without being logged in"""
        self.client.logout()
        self.client.credentials()
        test_pdf: File = ReportTestCase.load_test_pdf()
        response = self.client.post(
            reverse("report_upload"), {"uploaded_report": test_pdf}
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
