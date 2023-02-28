# -*- coding: utf-8 -*-
"""Module for SentenceManager"""
from typing import Dict

from api.grobid_tfidf_code.experiments import flatten_num_tokens, preprocess_text
from api.grobid_tfidf_code.main import split_into_sentences
from api.models.term_idf import TermIDF
from django.db.models import QuerySet
from django.db.models.manager import Manager
from django.utils import timezone


class SentenceManager(Manager):
    """Manager for creation of Sentence objects"""

    def __init__(self, *args, **kwargs):
        self.tf_idf_dict: Dict[str, float] = {}
        super().__init__(*args, **kwargs)

    def create(self, report, sentence_text: str, tf_idf_weight: float, *args, **kwargs):
        """Method to create a Sentence model from its text"""
        return super().create(
            *args,
            parent_report=report,
            text=sentence_text,
            tf_idf_weight=tf_idf_weight,
            **kwargs
        )

    def calculate_sentence_tfidf_weight(self, sentence: str) -> float:
        """Method used to calculate sentence_tfidf_weight for a given sentence in a given report"""
        tokens = preprocess_text(sentence, as_list=True)
        sentence_weight = 0.0
        for token in tokens:
            sentence_weight += self.tf_idf_dict.get(token, 0.0)

        # if tokens:
        #     return sentence_weight / len(tokens)
        if tokens:
            return sentence_weight
        return 0.0

    def extract_sentences(self, report) -> QuerySet:
        """
        Method to extract all sentences from a given report and calculate their tf_idf_weights

        Args:
            report: Report model to extract sentences from

        Returns:
            QuerySet of Sentence models created
        """
        self.tf_idf_dict = {}

        report.sentence_datetime = timezone.now()
        report.save()
        sentences = split_into_sentences(report.plaintext)
        report_tokens = preprocess_text(report.plaintext, as_list=True)
        term_frequency_dict = flatten_num_tokens([report_tokens])
        for term, frequency in term_frequency_dict.items():
            try:
                term_idf_model = TermIDF.objects.get(term=term)
            except TermIDF.DoesNotExist:
                term_idf_model = None
            term_idf = term_idf_model.idf if term_idf_model else 0.0
            self.tf_idf_dict[term] = frequency * term_idf

        for sentence in sentences:
            self.create(
                report=report,
                sentence_text=sentence,
                tf_idf_weight=self.calculate_sentence_tfidf_weight(sentence),
            )

        return report.sentences.all()
