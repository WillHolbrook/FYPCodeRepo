# -*- coding: utf-8 -*-
"""Module to test Profile updating and retrieval API"""
from api.tests.models.test_profile import ProfileTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestProfileViewCase(APITestCase):
    """Test Profile updating and retrieval API"""

    fixtures = ["profile_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_superuser_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_updating_profile(self):
        """Test for updating a profile"""
        image = ProfileTestCase.load_test_image()
        response = self.client.post(reverse("profile"), {"profile_image": image})

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNone(response.data["profile_image"])

    def test_non_logged_in_user_profile_update(self):
        """Test for updating a profile without being logged in"""
        self.client.logout()
        self.client.credentials()
        image = ProfileTestCase.load_test_image()
        response = self.client.post(reverse("profile"), {"profile_image": image})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieving_profile(self):
        """Test for retrieving a profile"""
        response = self.client.get(reverse("profile"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNone(response.data["profile_image"])

    def test_non_logged_in_user_profile_retrieval(self):
        """Test for retrieving a profile without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
