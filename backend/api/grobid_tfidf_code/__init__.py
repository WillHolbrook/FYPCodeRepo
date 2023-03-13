# -*- coding: utf-8 -*-
"""Module to make sure punkt dataset is installed"""
import nltk
from nltk.corpus import stopwords

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

STOPWORDS = stopwords.words("english")
