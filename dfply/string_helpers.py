from .base import *
import pandas as pd
import re
from numpy import NaN

# ------------------------------------------------------------------------------
# String helpers
# - a straight port of stringr
# ------------------------------------------------------------------------------

## Detect matches
# --------------------------------------------------
@make_symbolic
def str_detect(string, pattern):
    """
    Detect the presence of a pattern match in a string.
    """
    try:
        if isinstance(string, str):
            raise TypeError
        return pd.Series([not (re.search(pattern, s) is None) for s in string])

    except TypeError:
        return not (re.search(pattern, string) is None)

@make_symbolic
def str_locate(string, pattern):
    """
    Find the indices of all pattern matches.
    """
    try:
        if isinstance(string, str):
            raise TypeError
        return pd.Series(
            [[m.start(0) for m in re.finditer(pattern, s)] for s in string]
        )

    except TypeError:
        return [m.start(0) for m in re.finditer(pattern, string)]

def _safe_index(l, ind=0):
    try:
        return l[ind]
    except IndexError:
        return NaN

@make_symbolic
def str_which(string, pattern):
    """
    Find the index of the first pattern match.
    """
    indices = str_locate(string, pattern)

    try:
        if isinstance(string, str):
            raise TypeError
        return pd.Series([_safe_index(ind) for ind in indices])

    except TypeError:
        return _safe_index(indices)

@make_symbolic
def str_count(string, pattern):
    """
    Count the number of matches in a string.
    """
    indices = str_locate(string, pattern)

    try:
        if isinstance(string, str):
            raise TypeError
        return pd.Series([len(ind) for ind in indices])

    except TypeError:
        return len(indices)

## Subset strings
# --------------------------------------------------
