import pytest

from dfply import *
from numpy import isnan

##==============================================================================
## string helper tests
##==============================================================================

def test_str_detect():
    s_true = "foo"
    s_false = "bar"

    S_true = ["foo"]
    S_false = ["bar"]

    assert str_detect(s_true, "foo")
    assert not str_detect(s_false, "foo")

    assert all(str_detect(S_true, "foo"))
    assert not any(str_detect(S_false, "foo"))

def test_str_locate():
    s_ind0 = "foo"
    s_empty = "bar"

    S_ind0 = ["foo"]
    S_empty = ["bar"]

    R_ind0 = str_locate(S_ind0, "foo")
    R_empty = str_locate(S_empty, "foo")

    assert str_locate(s_ind0, "foo") == [0]
    assert len(str_locate(s_empty, "foo")) == 0

    assert R_ind0[0] == [0]
    assert len(R_empty[0]) == 0

def test_str_which():
    s_ind1 = "afoo"
    s_nan = "bar"

    S_ind1 = ["afoo"]
    S_nan = ["bar"]

    R_ind1 = str_which(S_ind1, "foo")
    R_nan = str_which(S_nan, "foo")

    assert str_which(s_ind1, "foo") == 1
    assert isnan(str_which(s_nan, "foo"))

    assert R_ind1[0] == 1
    assert isnan(R_nan[0])

def test_str_count():
    s_c2 = "foofoo"
    s_c0 = "bar"

    S_c2 = ["foofoo"]
    S_c0 = ["bar"]

    R_c2 = str_count(S_c2, "foo")
    R_c0 = str_count(S_c0, "foo")

    assert str_count(s_c2, "foo") == 2
    assert str_count(s_c0, "foo") == 0

    assert R_c2[0] == 2
    assert R_c0[0] == 0

def test_str_replace():

    assert str_replace("foofoo", "foo", "barbar") == "barbarfoo"
    assert str_replace("barbar", "foo", "bar") == "barbar"

    R = str_replace(["foo"], "foo", "bar")
    assert R[0] == "bar"
