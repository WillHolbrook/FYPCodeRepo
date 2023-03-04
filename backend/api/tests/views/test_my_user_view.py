# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
"""Module to test Report Upload API"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestReportUpload(APITestCase):
    """Test Report Upload API"""

    fixtures = ["profile_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_superuser_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_getting_user_details(self):
        """Test for getting user details"""
        response = self.client.get(reverse("my_user"))
        self.assertEqual(1, response.data["id"])
        self.assertEqual("test_superuser_username", response.data["username"])
        self.assertEqual(
            r"/profile_pictures/2023/02/test_YbbfNKm.jpg",
            response.data["profile"]["profile_image"],
        )

    def test_getting_non_logged_in_user(self):
        """Test for getting user details without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.get(reverse("my_user"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TODO # pylint: disable=fixme
    def test_updating_user_details(self):
        """Test for updating user details"""
        response = self.client.put(reverse("my_user"))
        self.assertTrue(False)

    def test_updating_non_logged_in_user(self):
        """Test for updating user details without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.put(reverse("my_user"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TODO # pylint: disable=fixme
    def test_deleting_user(self):
        """Test for updating user details"""
        response = self.client.delete(reverse("my_user"))
        self.assertTrue(False)

    def test_deleting_non_logged_in_user(self):
        """Test for updating user details without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.delete(reverse("my_user"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
