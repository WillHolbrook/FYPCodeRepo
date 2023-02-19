# -*- coding: utf-8 -*-
"""Module for SentenceManager"""
from api.grobid_tfidf_code.main import split_into_sentences
from django.db.models import QuerySet
from django.db.models.manager import Manager
from django.utils import timezone


class SentenceManager(Manager):  # pylint: disable=too-few-public-methods
    """Manager for creation of Sentence objects"""

    def create(
        self, report, sentence_text: str, tf_idf_weight: float, *args, **kwargs
    ):  # pylint: disable=unused-argument
        """Method to create a Sentence model from its text"""
        return super().create(
            *args,
            parent_report=report,
            text=sentence_text,
            tf_idf_weight=tf_idf_weight,
            **kwargs
        )

    # TODO # pylint: disable=fixme
    @staticmethod
    def calculate_sentence_tfidf_weight(
        report, sentence: str  # pylint: disable=unused-argument
    ) -> float:
        """Method used to calculate sentence_tfidf_weight for a given sentence in a given report"""
        return 0.0

    def extract_sentences(self, report) -> QuerySet:
        """
        Method to extract all sentences from a given report and calculate their tf_idf_weights

        Args:
            report: Report model to extract sentences from

        Returns:
            QuerySet of Sentence models created
        """
        report.sentence_datetime = timezone.now()
        report.save()
        sentences = split_into_sentences(report.plaintext)
        for sentence in sentences:
            self.create(
                report=report,
                sentence_text=sentence,
                tf_idf_weight=self.calculate_sentence_tfidf_weight(report, sentence),
            )

        return report.sentences.all()
