# -*- coding: utf-8 -*-
"""Module to contain File Model and associated methods"""
import xml.etree.ElementTree as ET

from api.grobid_tfidf_code.main import extract_text_from_element_tree
from api.managers.report_manager import ReportManager
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Report(models.Model):
    """Model to represent uploaded file and associated information"""

    objects = ReportManager()

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="reports", null=True
    )
    pdf = models.FileField(upload_to=f"reports/{user.primary_key}", null=False)
    tei_xml = models.TextField(null=False)
    plaintext = models.TextField(null=True, default=None)
    upload_datetime = models.DateTimeField(auto_now_add=True, null=False)
    last_modified = models.DateTimeField(auto_now=True, null=False)
    corpus_flag = models.BooleanField(default=False, null=False)
    in_idf_flag = models.BooleanField(default=False, null=False)
    plaintext_datetime = models.DateTimeField(null=True)
    sentence_datetime = models.DateTimeField(null=True)

    def extract_plaintext(self) -> None:
        """Method to extract plaintext from tei_xml and store it in the Report Body"""
        self.plaintext = extract_text_from_element_tree(ET.fromstring(self.tei_xml))
        self.plaintext_datetime = timezone.now()
        self.save()
