# -*- coding: utf-8 -*-
"""Module to contain File Model and associated methods"""

from api.managers.report_manager import ReportManager
from django.contrib.auth import get_user_model
from django.db import models


class Report(models.Model):
    """Model to represent uploaded file and associated information"""

    objects = ReportManager()

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="reports", null=True
    )
    tei_xml = models.TextField(null=False)
    plaintext = models.TextField(null=True, default=None)
    upload_datetime = models.DateTimeField(auto_now_add=True, null=False)
    last_modified = models.DateTimeField(auto_now=True, null=False)
    corpus_flag = models.BooleanField(default=True, null=False)
    in_idf_flag = models.BooleanField(default=False, null=False)
    plaintext_datetime = models.DateTimeField(null=True)
    sentence_datetime = models.DateTimeField(null=True)
