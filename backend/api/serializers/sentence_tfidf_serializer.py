# -*- coding: utf-8 -*-
"""Module for SentenceSerializer"""
from api.models.sentence import Sentence
from rest_framework import serializers


class SentenceSerializer(serializers.ModelSerializer):
    """Module to define how a Sentence is serialized"""

    class Meta:
        model = Sentence
        fields = [
            "text",
            "tf_idf_weight",
        ]
        extra_kwargs = {
            "text": {"read_only": True},
            "tf_idf_weight": {"read_only": True},
        }
