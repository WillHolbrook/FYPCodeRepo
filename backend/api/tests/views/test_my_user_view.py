# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
"""Module to test Report Upload API"""
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestReportUpload(APITestCase):
    """Test Report Upload API"""

    fixtures = ["user_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.username = "test_superuser_username"
        self.user = get_user_model().objects.get(username=self.username)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_getting_user_details(self):
        """Test for getting user details"""
        response = self.client.get(reverse("my_user"))
        self.assertEqual(1, response.data["id"])
        self.assertEqual(self.username, response.data["username"])
        self.assertIsNone(
            response.data["profile"]["profile_image"],
        )

    def test_getting_non_logged_in_user(self):
        """Test for getting user details without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.get(reverse("my_user"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_updating_user_details_without_username(self):
        """Test for updating user details"""
        new_password = "new_complex_password1A"
        response = self.client.put(reverse("my_user"), {"password": new_password})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], self.username)

        # Check logging in with new credentials
        self.client.logout()
        self.client.credentials()
        response2 = self.client.post(
            reverse("auth"), {"username": self.username, "password": new_password}
        )
        self.assertEqual(response2.status_code, 200)

    def test_updating_user_details_with_username(self):
        """Test for updating user details with username"""
        new_username = "new_amazing_username"
        new_password = "new_complex_password1A"
        response = self.client.put(
            reverse("my_user"), {"password": new_password, "username": new_username}
        )
        updated_user = get_user_model().objects.get(pk=self.user.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], new_username)
        self.assertEqual(response.data["username"], updated_user.username)
        self.assertEqual(new_username, updated_user.username)

        # Check logging in with new credentials
        response2 = self.client.post(
            reverse("auth"), {"username": new_username, "password": new_password}
        )
        self.assertEqual(response2.status_code, 200)

    def test_updating_non_logged_in_user(self):
        """Test for updating user details without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.put(reverse("my_user"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_deleting_user(self):
        """Test for updating user details"""
        response = self.client.delete(reverse("my_user"))
        # attempt to re-fetch profile from the database (should fail)
        with self.assertRaises(
            ObjectDoesNotExist, msg="User not deleted when delete method is called"
        ):
            get_user_model().objects.get(pk=self.user.pk)
        self.assertEqual(response.status_code, 204)

    def test_deleting_non_logged_in_user(self):
        """Test for updating user details without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.delete(reverse("my_user"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
