# -*- coding: utf-8 -*-
"""Module to contain File Model and associated methods"""

from api.managers.report_manager import ReportManager
from django.contrib.auth import get_user_model
from django.db import models


class Report(models.Model):
    """Model to represent uploaded file and associated information"""

    objects = ReportManager()

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="user_files", null=True
    )
