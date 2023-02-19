# -*- coding: utf-8 -*-
"""Module for Report ViewSet"""
from api.models.report import Report
from api.serializers.user_report_details_serializer import ReportDetailSerializer
from api.serializers.user_report_list_serializer import ReportListSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ReportViewSet(
    viewsets.ReadOnlyModelViewSet
):  # pylint: disable=too-many-ancestors
    """Reports ViewSet for end Users"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReportDetailSerializer
    queryset = Report.objects.all()

    action_serializers = {"list": ReportListSerializer}

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return []

        return self.queryset.filter(user=self.request.user.id)

    def get_serializer_class(self):

        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super().get_serializer_class()
