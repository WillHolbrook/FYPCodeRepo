# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
"""Module to test Report Upload API"""
from api.models.report import Report
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestAddToCorpus(APITestCase):
    """Test Add to Corpus API"""

    fixtures = ["user_fixtures.json", "report_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_superuser_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_add_report_to_corpus(self):
        """Test adding a report to a corpus"""
        report_count = Report.objects.count()
        report_pk = 3
        initial_report = Report.objects.get(pk=report_pk)
        initial_report.extract_plaintext()
        response = self.client.post(
            reverse("add_to_corpus", kwargs={"report_pk": report_pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(report_count + 1, Report.objects.count())
        self.assertNotEqual(response.data["report_pk"], report_pk)

        duplicate_report = Report.objects.get(pk=response.data["report_pk"])
        self.assertIsNone(duplicate_report.user)
        self.assertEqual(duplicate_report.tei_xml, initial_report.tei_xml)
        self.assertEqual(duplicate_report.plaintext, initial_report.plaintext)

    def test_unowned_report(self):
        """Test for add_to_corpus for unowned file"""
        report_pk = 2
        response = self.client.post(
            reverse("add_to_corpus", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_existing_report(self):
        """Test for add_to_corpus for non-existing file"""
        report_pk = 4
        response = self.client.post(
            reverse("add_to_corpus", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_logged_in_user(self):
        """Test for uploading a report without being logged in"""
        self.client.logout()
        self.client.credentials()
        report_pk = 3
        response = self.client.post(
            reverse("add_to_corpus", kwargs={"report_pk": report_pk})
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_admin_user(self):
        """Test for uploading a report without being logged in"""
        self.user = get_user_model().objects.get(username="test_user_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        report_pk = 2
        response = self.client.post(
            reverse("add_to_corpus", kwargs={"report_pk": report_pk})
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
