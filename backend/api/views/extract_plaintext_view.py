# -*- coding: utf-8 -*-
"""Module for ExtractPlaintextView"""
from api.serializers.report_details_serializer import ReportDetailSerializer
from api.views.auth_utils import check_user_is_present_and_has_access_to_given_report
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ExtractPlaintextView(APIView):
    """View to add (re)extract plaintext from a given report"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, report_pk):
        """
        Method executed when a post request is received
        to rextract the report plaintext

        Args:
            request:
            report_pk: The Primary Key of the Report to extract

        Returns:
            the updated file
        """
        (response, report) = check_user_is_present_and_has_access_to_given_report(
            request, report_pk
        )
        if report is None:
            return response

        # Extract the plaintext to make sure it's up-to-date
        report.extract_plaintext()
        return Response(ReportDetailSerializer(report).data, status=status.HTTP_200_OK)
