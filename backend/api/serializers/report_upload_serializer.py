# -*- coding: utf-8 -*-
"""Module for Serialization of uploading a report"""
from api.models.report import Report
from django.core.exceptions import BadRequest
from rest_framework import serializers


class UserReportUploadSerializer(serializers.Serializer):
    """Serializer for uploading a report"""

    def update(self, instance, validated_data):
        raise BadRequest("This function shouldn't be called to update a Report")

    uploaded_report = serializers.FileField()

    def create(self, validated_data):
        return Report.objects.create(
            report_file=validated_data["uploaded_report"], user=validated_data["user"]
        )
