# -*- coding: utf-8 -*-
"""Module to test extract plaintext API"""
from api.models.report import Report
from api.tests.models.test_sentence import SentenceTestCase
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
        self.user = get_user_model().objects.get(username="test_user_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_extracting_plaintext(self):
        """Test extracting plaintext from a report"""
        report = (
            Report.objects._create_without_file(  # pylint: disable=protected-access
                tei_xml=SentenceTestCase.tei_xml, plaintext="", user=self.user
            )
        )
        report_pk = report.pk
        response = self.client.post(
            reverse("extract_plaintext", kwargs={"report_pk": report_pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data["plaintext"], "")

    def test_unowned_report(self):
        """Test for add_to_corpus for unowned file"""
        report_pk = 3
        response = self.client.post(
            reverse("extract_plaintext", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_existing_report(self):
        """Test for add_to_corpus for non-existing file"""
        report_pk = 4
        response = self.client.post(
            reverse("extract_plaintext", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_logged_in_user(self):
        """Test for uploading a report without being logged in"""
        self.client.logout()
        self.client.credentials()
        report_pk = 3
        response = self.client.post(
            reverse("extract_plaintext", kwargs={"report_pk": report_pk})
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
