# -*- coding: utf-8 -*-
"""Module to test Report API"""
from api.models.report import Report
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestReportRetrieve(APITestCase):
    """Test Report Retrieval API"""

    fixtures = ["user_fixtures.json", "report_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_user_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_singular_report(self):
        """Test for retrieving a report"""
        report_pk = 2
        response = self.client.get(reverse("reports-detail", kwargs={"pk": report_pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        report = Report.objects.get(pk=report_pk)

        report_data = response.data

        self.assertEqual(report_data["tei_xml"], report.tei_xml)
        self.assertEqual(report_data["plaintext"], report.plaintext)

    def test_non_owned_report(self):
        """Test for extracting sentences from an unowned report"""
        report_pk = 3
        response = self.client.get(reverse("reports-detail", kwargs={"pk": report_pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_existing_report(self):
        """Test for extracting sentences from a non-existent report"""
        report_pk = 4
        response = self.client.get(reverse("reports-detail", kwargs={"pk": report_pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_logged_in_user(self):
        """Test for extracting a report without being logged in"""
        report_pk = 2
        self.client.logout()
        self.client.credentials()
        response = self.client.get(reverse("reports-detail", kwargs={"pk": report_pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestReportList(APITestCase):
    """Test Report List API"""

    fixtures = ["user_fixtures.json", "report_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_user_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        self.reports = self.user.reports.all()

    def test_list(self):
        """Test for retrieving a list of reports"""
        response = self.client.get(reverse("reports-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        list_data = response.data

        self.assertEqual(list_data["count"], 2)

        reports_list = list_data["results"]
        reports_pk_list = [report.pk for report in self.reports]
        for report in reports_list:
            self.assertIn(report["pk"], reports_pk_list)

    def test_no_reports(self):
        """Test for response when there are no reports"""
        created_user = get_user_model().objects.create_user("user2", "password")
        token = Token.objects.create(user=created_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        response = self.client.get(reverse("reports-list"))

        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

    def test_non_logged_in_user(self):
        """Test for extracting a report without being logged in"""
        self.client.logout()
        self.client.credentials()
        response = self.client.get(reverse("reports-list"))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestReportDelete(APITestCase):
    """Test Report Delete API"""

    fixtures = ["user_fixtures.json", "report_fixtures.json"]

    def setUp(self) -> None:
        """Run before each test"""
        self.client = APIClient()
        self.user = get_user_model().objects.get(username="test_user_username")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_delete(self):
        """Test for deleting a report"""
        report_pk = 2
        response = self.client.delete(
            reverse("reports-detail", kwargs={"pk": report_pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_unowned_report(self):
        """Test for deleting a report a user doesn't own"""
        report_pk = 3
        response = self.client.delete(
            reverse("reports-detail", kwargs={"pk": report_pk})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_non_existing_report(self):
        """Test for deleting a report that doesn't exist"""
        report_pk = 4
        response = self.client.delete(
            reverse("reports-detail", kwargs={"pk": report_pk})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_logged_in_user(self):
        """Test for extracting a report without being logged in"""
        self.client.logout()
        self.client.credentials()
        report_pk = 4
        response = self.client.delete(
            reverse("reports-detail", kwargs={"pk": report_pk})
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
