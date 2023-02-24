# -*- coding: utf-8 -*-
"""Module for AddReportToCorpusView"""
from api.models.report import Report
from api.views.auth_utils import check_user_is_present_and_has_access_to_given_report
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AddReportToCorpusView(APIView):
    """View to add a copy of a report to a corpus"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, report_pk):
        """
        Method executed when a post request is received
        to add a copy of the report to the corpus

        Args:
            request:
            report_pk: The Primary Key of the Report to extract

        Returns:
            status.HTTP_204_NO_CONTENT if the report is copied and added to the database
        """
        (response, report) = check_user_is_present_and_has_access_to_given_report(
            request, report_pk
        )
        if report is None:
            return response

        new_report: Report = report
        new_report.pk = None
        new_report.corpus_flag = True
        new_report.user = None
        new_report.save()

        return Response({"report_pk": new_report.pk}, status=status.HTTP_200_OK)
