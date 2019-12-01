import pytest

from dfply import *

##==============================================================================
## mask helper tests
##==============================================================================

def test_var_in():
    df = diamonds[['cut']].head(10)
    d1 = df[(df.cut == "Ideal") | (df.cut == "Premium")]
    d2 = df >> mask(var_in(X.cut, ["Ideal", "Premium"]))

    assert d1.equals(d2)
