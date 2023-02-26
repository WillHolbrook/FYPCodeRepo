# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
"""Module to test calculating the IDF"""
from api.models.report import Report
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestCalculateIDF(APITestCase):
    """Test calculating the IDF API"""

    fixtures = ["user_fixtures.json", "report_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_superuser_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_calculate_idf(self):
        """Test calculating the IDF"""
        response = self.client.post(reverse("calculate_idf"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["num_reports"], 3)

    def test_calculate_idf_with_no_reports_in_corpus(self):
        """Test calculating the IDF"""
        Report.objects.all().delete()
        response = self.client.post(reverse("calculate_idf"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["num_reports"], 0)
        self.assertEqual(response.data["num_terms"], 0)

    def test_non_logged_in_user(self):
        """Test for calculating the IDF without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.post(reverse("calculate_idf"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_admin_user(self):
        """Test for calculating the IDF without being logged in"""
        self.user = get_user_model().objects.get(username="test_user_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        response = self.client.post(reverse("calculate_idf"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
