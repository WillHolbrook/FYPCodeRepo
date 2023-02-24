# -*- coding: utf-8 -*-
# pylint: skip-file
from __future__ import annotations

import string
from datetime import datetime
from functools import wraps
from multiprocessing.pool import Pool
from multiprocessing.spawn import freeze_support
from pathlib import Path

import nltk
import numpy as np
from nltk import PorterStemmer, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.api import StemmerI


def print_dict_ordered_on_keys(d: dict, reverse: bool = True) -> None:
    """
    Prints a dictionary ordered based on the keys

    Args:
        d: the dictionary to predict
        reverse: a flag to say whether to reverse the sort or not

    Returns:
        None
    """
    print(
        {
            term: frequency
            for term, frequency in sorted(
                d.items(), key=lambda x: x[1], reverse=reverse
            )
        }
    )


def log_time(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        total_time = end_time - start_time
        print(f"Function {func.__name__} Took {total_time}")
        return result

    return timeit_wrapper


def preprocess_text(
    text_or_filepath: str | Path,
    stemmer: StemmerI = PorterStemmer(),
    as_list: bool = False,
) -> list[str] | set[str]:
    """
    Pre-processes text by:
        removing punctuation
        tokenizing the string
        removing stop words
        stemming tokens to common roots

    Args:
        text_or_filepath: the text or the filepath to the file containing the text to run pre-processing on
        stemmer: the stemmer to use if not given a default stemmer of the nltk.stem.porter.PorterStemmer is used
        as_list: if true will calculate and return values as a list else will calculate and return as a set

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
            doc_token
            for doc_token in doc_tokens
            if doc_token not in stopwords.words("english")
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


@log_time
def calculate_idf_for_corpus(
    root_folder_path: Path,
) -> tuple[dict[str, int], dict[str, float], int]:
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
    term_doc_count = dict()
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
) -> tuple[dict[str, int], dict[str, float], int]:
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
    term_doc_count = dict()
    filepaths = [
        filepath for filepath in root_folder_path.rglob("*.txt") if filepath.is_file()
    ]
    num_docs = len(filepaths)
    num_processes = min(max_num_processes, num_docs)

    if num_processes > 0:
        with Pool(num_processes) as pool:
            doc_tokens_list: list[set[str]] = pool.map(preprocess_text, filepaths)

    for doc_tokens in doc_tokens_list:
        for token in doc_tokens:
            if token in term_doc_count:
                term_doc_count[token] += 1
            else:
                term_doc_count[token] = 1

    idf = {
        term: np.log(num_docs / frequency) for term, frequency in term_doc_count.items()
    }
    return idf, term_doc_count, num_docs


def main():
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)

    freeze_support()
    root_folder_path = Path("../../../../FilestoreRepo/FTSE100Info/txtReports/3i_group")
    idf_s, term_count_s, num_docs_s = calculate_idf_for_corpus(root_folder_path)
    print_dict_ordered_on_keys(idf_s)
    print_dict_ordered_on_keys(term_count_s)

    print("\n======================================================================\n")

    idf_p, term_count_p, num_docs_p = calculate_idf_for_corpus_parallel(
        root_folder_path, max_num_processes=8
    )
    print_dict_ordered_on_keys(idf_p)
    print_dict_ordered_on_keys(term_count_p)
    print(f"Number of docs processed {num_docs_p}")

    print(f"idf_s == idf_p is {idf_s == idf_p}")
    print(f"term_count_s == term_count_p is {term_count_s == term_count_p}")
    print(f"num_docs_s == num_docs_p is {num_docs_s == num_docs_p}")


if __name__ == "__main__":
    main()
