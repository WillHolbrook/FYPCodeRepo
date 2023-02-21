# -*- coding: utf-8 -*-
"""Module to test ExtractSentence API"""
from api.models.report import Report
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestExtractSentences(APITestCase):
    """Test ExtractSentence API"""

    fixtures = ["user_fixtures.json", "report_fixtures.json", "sentence_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_user_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_extract_sentences(self):
        """Test for extracting sentences"""
        report_pk = 2
        response = self.client.post(
            reverse("extract_sentence", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        paged_response = response.data
        num_returned_sentences = paged_response["count"]

        self.assertGreaterEqual(num_returned_sentences, 4)
        self.assertIsNone(paged_response["next"])
        self.assertIsNone(paged_response["previous"])

        report = Report.objects.get(user=self.user, pk=report_pk)
        sentences = report.sentences.all()

        self.assertEqual(len(sentences), num_returned_sentences)

        returned_sentence_text = [
            result["text"] for result in paged_response["results"]
        ]
        for sentence in sentences:
            self.assertIn(sentence.text, returned_sentence_text)

    def test_extracting_non_owned_report(self):
        """Test for extracting sentences from an unowned report"""
        report_pk = 3
        response = self.client.post(
            reverse("extract_sentence", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_extracting_non_existing_report(self):
        """Test for extracting sentences from a non-existent report"""
        report_pk = 4
        response = self.client.post(
            reverse("extract_sentence", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_logged_in_user(self):
        """Test for extracting a report without being logged in"""
        report_pk = 2
        self.client.logout()
        self.client.credentials()
        response = self.client.post(
            reverse("extract_sentence", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_getting_sentences(self):
        """Test for retrieving extracted sentences"""
        report_pk = 1
        response = self.client.get(
            reverse("extract_sentence", kwargs={"report_pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
