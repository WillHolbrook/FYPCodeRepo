# -*- coding: utf-8 -*-
"""Module to contain the Sentence Model and associated methods"""
from api.managers.sentence_manager import SentenceManager
from api.models.report import Report
from django.db import models


class Sentence(models.Model):
    """Model to represnt Sentences extracted from reports"""

    objects = SentenceManager()

    parent_report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name="sentences"
    )

    text = models.TextField(null=False)
    tf_idf_weight = models.FloatField(null=False, default=0.0)
