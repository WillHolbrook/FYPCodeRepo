# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
"""Module for ReportSerializer"""
from api.models.report import Report
from rest_framework import serializers


class ReportDetailSerializer(serializers.ModelSerializer):
    """Module to define how a general report is serialized"""

    class Meta:
        model = Report
        fields = [
            "pk",
            "pdf",
            "tei_xml",
            "plaintext",
            "upload_datetime",
            "last_modified",
            "plaintext_datetime",
            "sentence_datetime",
            "buy_sell_hold",
        ]
        extra_kwargs = {
            "pk": {"read_only": True},
            "pdf": {"read_only": True},
            "tei_xml": {"read_only": True},
            "plaintext": {"read_only": True},
            "upload_datetime": {"read_only": True},
            "last_modified": {"read_only": True},
            "plaintext_datetime": {"read_only": True},
            "sentence_datetime": {"read_only": True},
            "buy_sell_hold": {"read_only": True},
        }
