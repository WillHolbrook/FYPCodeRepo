# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
"""Module for ReportSerializer"""
from api.models.report import Report
from rest_framework import serializers


class ReportListSerializer(serializers.ModelSerializer):
    """Module to define how a general report is serialized"""

    class Meta:
        model = Report
        fields = [
            "pk",
            "report_name",
            "upload_datetime",
            "last_modified",
            "plaintext_datetime",
            "sentence_datetime",
        ]
        extra_kwargs = {
            "pk": {"read_only": True},
            "report_name": {"read_only": True},
            "upload_datetime": {"read_only": True},
            "last_modified": {"read_only": True},
            "plaintext_datetime": {"read_only": True},
            "sentence_datetime": {"read_only": True},
        }
