# -*- coding: utf-8 -*-
"""Module for UserReportExtractSentenceView"""
from __future__ import annotations

from api.models.sentence import Sentence
from api.serializers.sentence_serializer import SentenceSerializer
from api.views.auth_utils import check_user_is_present_and_has_access_to_given_report
from django.db.models import QuerySet
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
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
        (response, report) = check_user_is_present_and_has_access_to_given_report(
            request, report_pk
        )
        if report is None:
            return response
        return self._get_paginated_sentence(request, report.sentences.all())
