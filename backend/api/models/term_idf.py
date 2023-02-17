# -*- coding: utf-8 -*-
"""Module to contain the TermIDF Model and associated methods"""
from django.db import models


class TermIDF(models.Model):
    """Model to represnt Sentences extracted from reports"""

    term = models.TextField(null=False)
    term_frequency = models.IntegerField(null=False, default=0)
    idf = models.FloatField(null=False, default=0.0)
