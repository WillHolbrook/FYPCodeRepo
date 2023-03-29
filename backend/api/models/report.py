# -*- coding: utf-8 -*-
"""Module to contain File Model and associated methods"""
import xml.etree.ElementTree as ET
from typing import List, Set, Union

from api.grobid_tfidf_code.experiments import flatten_num_tokens, preprocess_text
from api.grobid_tfidf_code.main import extract_text_from_element_tree
from api.managers.report_manager import ReportManager
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from nltk import PorterStemmer, StemmerI


class Report(models.Model):
    """Model to represent uploaded file and associated information"""

    objects = ReportManager()

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="reports", null=True
    )
    report_name = models.CharField(max_length=100, null=False, blank=False)
    pdf = models.FileField(upload_to=f"reports/{user.primary_key}", null=False)
    tei_xml = models.TextField(null=False)
    plaintext = models.TextField(null=True, default=None)
    upload_datetime = models.DateTimeField(auto_now_add=True, null=False)
    last_modified = models.DateTimeField(auto_now=True, null=False)
    corpus_flag = models.BooleanField(default=False, null=False)
    in_idf_flag = models.BooleanField(default=False, null=False)
    plaintext_datetime = models.DateTimeField(null=True)
    sentence_datetime = models.DateTimeField(null=True)

    BUY_SELL_HOLD_CHOICES = (
        ("Buy", "Buy"),
        ("Sell", "Sell"),
        ("Hold", "Hold"),
    )

    buy_sell_hold = models.CharField(
        max_length=4,
        choices=BUY_SELL_HOLD_CHOICES,
        null=True,
        default=None,
    )

    class Meta:
        ordering = ["-last_modified"]

    buy_aliases = {"buy", "overweight", "ow", "po", "posit"}
    sell_aliases = {"sell", "underweight", "uw", "neg"}
    hold_aliases = {"balanced", "neutral", "equal", "neu", "ew"}

    @staticmethod
    def extract_terms(
        report_id,
        stemmer: StemmerI = PorterStemmer(),
    ) -> Union[List[str], Set[str]]:
        """Function to extract the unique terms used in a report"""

        report = Report.objects.get(pk=report_id)
        if report.plaintext is None:
            report.extract_plaintext()
        return preprocess_text(report.plaintext, stemmer=stemmer)

    def extract_plaintext(self) -> None:
        """Method to extract plaintext from tei_xml and store it in the Report Body"""
        self.plaintext = extract_text_from_element_tree(ET.fromstring(self.tei_xml))
        self.plaintext_datetime = timezone.now()
        self.save()

    def extract_buy_sell_hold(self) -> None:
        """Method to extract buy sell hold from a given report"""
        tokens = preprocess_text(self.plaintext, as_list=True)
        term_frequency_dict = flatten_num_tokens([tokens])
        num_buy_aliases = 0
        num_sell_aliases = 0
        num_hold_aliases = 0

        for buy_alias in self.buy_aliases:
            num_buy_aliases += term_frequency_dict.get(buy_alias, 0)

        for sell_alias in self.sell_aliases:
            num_sell_aliases += term_frequency_dict.get(sell_alias, 0)

        for hold_alias in self.hold_aliases:
            num_hold_aliases += term_frequency_dict.get(hold_alias, 0)

        if num_buy_aliases > num_sell_aliases and num_buy_aliases > num_hold_aliases:
            # More buy aliases than any other
            self.buy_sell_hold = "Buy"
        elif num_sell_aliases > num_hold_aliases:
            # More sell aliases than any other
            self.buy_sell_hold = "Sell"
        else:
            # More hold aliases than any other
            self.buy_sell_hold = "Hold"

    def save(self, *args, **kwargs):
        if self.plaintext is None:
            self.plaintext = extract_text_from_element_tree(ET.fromstring(self.tei_xml))
            self.plaintext_datetime = timezone.now()
        self.extract_buy_sell_hold()
        super().save(*args, **kwargs)
