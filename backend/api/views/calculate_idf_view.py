# -*- coding: utf-8 -*-
"""Module for CalculateIDF"""
from multiprocessing.pool import Pool
from typing import List, Set, Tuple

import numpy as np
from api.grobid_tfidf_code.experiments import flatten_num_tokens, preprocess_report
from api.models.report import Report
from api.models.term_idf import TermIDF
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CalculateIDF(APIView):
    """View to add a copy of a report to a corpus"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        """
        Method executed when a post request is received
        to calculate idf of every document in the corpus

        Args:
            request:

        Returns:
            status. if the report is copied and added to the database
        """
        num_terms, num_reports = self.calculate_idf_for_corpus_parallel_django()

        return Response(
            {"num_terms": num_terms, "num_reports": num_reports},
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def calculate_idf_for_corpus_parallel_django(
        max_num_processes: int = 8,
    ) -> Tuple[int, int]:
        """
        calculates the idf of terms from all Report objects marked with the in corpus flag

        Args:
            max_num_processes: the maximum number of processes used in calculations
            max_reports_in_memory: the maximum number of report plaintext in memory at once


        Returns:
            A tuple of:
            The number of terms in the vocabulary
            The number of Reports extracted from
        """
        corpus_report_ids = list(
            Report.objects.filter(corpus_flag=True).values_list("id", flat=True)
        )
        num_docs = len(corpus_report_ids)
        doc_tokens_list: List[Set[str]] = []

        num_processes = min(max_num_processes, num_docs)

        if num_processes > 0:
            with Pool(num_processes) as pool:
                doc_tokens_list: List[Set[str]] = pool.map(
                    preprocess_report, corpus_report_ids
                )

        doc_tokens = flatten_num_tokens(doc_tokens_list)

        idf_models: List[TermIDF] = []
        for term, frequency in doc_tokens.items():
            # Note we add 1 to the frequency to smooth errors
            idf_models.append(
                TermIDF(
                    term=term,
                    term_frequency=frequency,
                    idf=np.log10(num_docs / frequency + 1),
                )
            )

        TermIDF.objects.all().delete()
        for model in idf_models:
            model.save()

        return len(idf_models), num_docs
