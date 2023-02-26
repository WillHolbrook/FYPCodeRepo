# -*- coding: utf-8 -*-
"""Module to make sure punkt dataset is installed"""
import nltk

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
