# -*- coding: utf-8 -*-
"""Module for UserReportExtractSentenceView"""
from api.views.auth_utils import check_user_is_present_and_has_access_to_given_report
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from summarizer import Summarizer


class UserReportExtractSentenceView(APIView):
    """View to extract sentences from a report and retrieve extracted sentences"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    model = Summarizer()

    def _extract_sentences_using_bert(self):
        """Method to extract sentences using BERT"""

    def post(self, request, report_pk):
        """
        Method executed when a post request is received
        to extract sentences from a given report

        Args:
            request:
            report_pk: The Primary Key of the Report to extract

        Returns:
            A paginated response of the extracted sentences if the user owns the given report
        """
        (response, report) = check_user_is_present_and_has_access_to_given_report(
            request, report_pk
        )
        if report is None:
            return response

        # Extract the plaintext if it isn't already extracted
        if report.plaintext is None:
            report.extract_plaintext()

        return None

    def get(self, request, report_pk):
        """
        Method executed when a get request is received
        to return extracted sentences from a given report

        Args:
            request:
            report_pk: The Primary Key of the Report to get sentences from

        Returns:
            A paginated response of the sentences if the user owns the given report
        """
        (response, report) = check_user_is_present_and_has_access_to_given_report(
            request, report_pk
        )
        if report is None:
            return response

        return None
