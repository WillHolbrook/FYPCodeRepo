# -*- coding: utf-8 -*-
"""Module Containing functions used in calculation of tf_idf"""
import string
from datetime import datetime
from functools import wraps
from multiprocessing.pool import Pool
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple, Union

import numpy as np
from api.grobid_tfidf_code import STOPWORDS
from nltk import PorterStemmer, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.api import StemmerI


def print_dict_ordered_on_keys(dictionary: dict, reverse: bool = True) -> None:
    """
    Prints a dictionary ordered based on the keys

    Args:
        dictionary: the dictionary to print
        reverse: a flag to say whether to reverse the sort or not

    Returns:
        None
    """
    print(dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse)))


def log_time(func):
    """Method to print the execution time of the wrapped function"""

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        """Time wrapper function"""
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        total_time = end_time - start_time
        print(f"Function {func.__name__} Took {total_time}")
        return result

    return timeit_wrapper


def preprocess_text(
    text_or_filepath: Union[str, Path],
    stemmer: StemmerI = PorterStemmer(),
    as_list: bool = False,
) -> Union[List[str], Set[str]]:
    """
    Pre-processes text by:
        removing punctuation
        tokenizing the string
        removing stop words
        stemming tokens to common roots

    Args:
        text_or_filepath: the text or the filepath to the file
            containing the text to run pre-processing on
        stemmer: the stemmer to use if not given a default stemmer
            of the nltk.stem.porter.PorterStemmer is used
        as_list: if true will calculate and return values as a
            list else will calculate and return as a set

    Returns:
        Either a list or a set of all pre-processed tokens in the text
        If a list it will have the number of duplicate terms as occur in the text
    """
    if isinstance(text_or_filepath, Path):
        if not text_or_filepath.is_file():
            print(f"filepath {text_or_filepath.resolve()} doesn't point to a file")
        with open(text_or_filepath, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = text_or_filepath

    # Replace all punctuation with white space and make lower case
    text = "".join([" " if t in string.punctuation else t for t in text]).lower()
    if as_list:
        # Return tokens as a list
        # Split into tokens
        doc_tokens = word_tokenize(text)
        # Remove Stopwords
        doc_tokens = [
            doc_token for doc_token in doc_tokens if doc_token not in STOPWORDS
        ]
        # Stem Tokens
        doc_tokens = [stemmer.stem(doc_token) for doc_token in doc_tokens]
    else:
        # Return tokens as a set
        # Split into tokens
        doc_tokens = set(word_tokenize(text))
        # Remove Stopwords
        doc_tokens = {
            doc_token
            for doc_token in doc_tokens
            if doc_token not in stopwords.words("english")
        }
        # Stem Tokens
        doc_tokens = {stemmer.stem(doc_token) for doc_token in doc_tokens}
    return doc_tokens


def flatten_num_tokens(tokens_list: List[Iterable[str]]) -> Dict[str, int]:
    """
    Method to count term document frequency from a list of set of terms in each document
    Args:
        tokens_list:

    Returns:
        A dict from term to document frequency of that term
    """
    term_doc_count = {}
    for doc_tokens in tokens_list:
        for token in doc_tokens:
            if token in term_doc_count:
                term_doc_count[token] += 1
            else:
                term_doc_count[token] = 1
    return term_doc_count


@log_time
def calculate_idf_for_corpus(
    root_folder_path: Path,
) -> Tuple[Dict[str, int], Dict[str, float], int]:
    """
    calculates the idf of terms from all .txt files beneath the folder path given

    Args:
        root_folder_path: the Path object to the folder that contains the txt files to be analyzed

    Returns:
        A tuple of 3 objects containing:
        1. A dictionary from term to inverse document frequency
        2. A dictionary from term to count of number of documents it occurs in
        3. The count of number of documents analyzed
    """
    term_doc_count = {}
    num_docs = 0
    for filepath in root_folder_path.rglob("*.txt"):
        if filepath.is_file():
            num_docs += 1
            with open(filepath, "r", encoding="utf-8") as f:
                document = f.read()
            doc_tokens = preprocess_text(document, as_list=False)
            for token in doc_tokens:
                if token in term_doc_count:
                    term_doc_count[token] += 1
                else:
                    term_doc_count[token] = 1

    idf = {
        term: np.log(num_docs / frequency) for term, frequency in term_doc_count.items()
    }
    return idf, term_doc_count, num_docs


@log_time
def calculate_idf_for_corpus_parallel(
    root_folder_path: Path, max_num_processes: int = 8
) -> Tuple[Dict[str, int], Dict[str, float], int]:
    """
    calculates the idf of terms from all .txt files beneath the folder path given in parallel

    Args:
        max_num_processes: the maximum number of processes used in calculations
        root_folder_path: the Path object to the folder that contains the txt files to be analyzed

    Returns:
        A tuple of 3 objects containing:
        1. A dictionary from term to inverse document frequency
        2. A dictionary from term to count of number of documents it occurs in
        3. The count of number of documents analyzed
    """
    filepaths = [
        filepath for filepath in root_folder_path.rglob("*.txt") if filepath.is_file()
    ]
    num_docs = len(filepaths)
    num_processes = min(max_num_processes, num_docs)

    if num_processes > 0:
        with Pool(num_processes) as pool:
            doc_tokens_list: List[Set[str]] = pool.map(preprocess_text, filepaths)

    term_doc_count = flatten_num_tokens(doc_tokens_list)

    idf = {
        term: np.log(num_docs / frequency) for term, frequency in term_doc_count.items()
    }
    return idf, term_doc_count, num_docs
