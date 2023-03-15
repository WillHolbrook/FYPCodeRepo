# -*- coding: utf-8 -*-
"""Module to make sure punkt dataset is installed"""
import logging
import os

import nltk
from nltk.corpus import stopwords

logger = logging.getLogger("django")
download_path = os.getenv("NLTK_DATA_DIR", default=None)
logger.info("Download path is %s", download_path)
if download_path is not None:
    nltk.data.path.append(download_path)

nltk.download("punkt", quiet=True, download_dir=download_path)
nltk.download("stopwords", quiet=True, download_dir=download_path)

STOPWORDS = stopwords.words("english")
