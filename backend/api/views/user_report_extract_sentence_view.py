# -*- coding: utf-8 -*-
"""Module for UserReportExtractSentenceView"""
from __future__ import annotations

from api.models.report import Report
from api.models.sentence import Sentence
from api.serializers.sentence_serializer import SentenceSerializer
from api.views.auth_utils import check_user_not_anon
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class UserReportExtractSentenceView(APIView, LimitOffsetPagination):
    """View to extract sentences from a report and retrieve extracted sentences"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def _get_paginated_sentence(self, request, sentences: QuerySet[Sentence]):
        """Method to get a paginated response used in both post() and get()"""
        results = self.paginate_queryset(sentences, request, view=self)
        serializer = SentenceSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    @staticmethod
    def check_user_is_present_and_has_access_to_given_report(
        request, report_pk: int
    ) -> tuple[Response, None] | tuple[None, Report]:
        """
        Method to check if a user is present and has access to a given report

        Args:
            request:
            report_pk: The Primary Key of the Report to extract

        Returns:
            error Response, None - if the user isn't provided or the specified report
                doesn't exist/they don't own the report
            None, Report - If the user is provided, and they have access to the specified report
        """
        user_anon_resp = check_user_not_anon(request)
        if user_anon_resp:
            return user_anon_resp, None
        try:
            report = Report.objects.get(pk=report_pk, user=request.user.id)
            return None, report
        except Report.DoesNotExist:
            return (
                Response(
                    data={"message": "Report doesn't exist"},
                    status=status.HTTP_404_NOT_FOUND,
                ),
                None,
            )

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
        response, report = self.check_user_is_present_and_has_access_to_given_report(
            request, report_pk
        )
        if report is None:
            return response

        # Extract the plaintext if it isn't already extracted
        if report.plaintext is None:
            report.extract_plaintext()

        # Delete all existing sentences
        report.sentences.all().delete()
        sentences = Sentence.objects.extract_sentences(report)
        return self._get_paginated_sentence(request, sentences)

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
        response, report = self.check_user_is_present_and_has_access_to_given_report(
            request, report_pk
        )
        if report is None:
            return response
        return self._get_paginated_sentence(request, report.sentences.all())
