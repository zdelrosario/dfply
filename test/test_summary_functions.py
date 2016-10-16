import pytest

from dfply import *


##==============================================================================
## transform summary functions
##==============================================================================

def test_mean():
    df = diamonds >> select(X.cut, X.x) >> head(5)
    # straight summarize
    t = df >> summarize(m=mean(X.x))
    df_truth = pd.DataFrame({'m': [4.086]})
    assert t.equals(df_truth)
    # grouped summarize
    t = df >> groupby(X.cut) >> summarize(m=mean(X.x))
    df_truth = pd.DataFrame({'cut': ['Good', 'Ideal', 'Premium'],
                             'm': [4.195, 3.950, 4.045]})
    assert t.equals(df_truth)
    # straight mutate
    t = df >> mutate(m=mean(X.x))
    df_truth = df.copy()
    df_truth['m'] = df_truth.x.mean()
    assert t.equals(df_truth)
    # grouped mutate
    t = df >> groupby(X.cut) >> mutate(m=mean(X.x))
    df_truth['m'] = pd.Series([3.950, 4.045, 4.195, 4.045, 4.195])
    assert t.equals(df_truth)


def test_first():
    df = diamonds >> select(X.cut, X.x) >> head(5)
    # straight summarize
    t = df >> summarize(f=first(X.x))
    df_truth = pd.DataFrame({'f': [3.95]})
    assert t.equals(df_truth)
    # grouped summarize
    t = df >> groupby(X.cut) >> summarize(m=mean(X.x))
    df_truth = pd.DataFrame({'cut': ['Good', 'Ideal', 'Premium'],
                             'm': [4.195, 3.950, 4.045]})
    assert t.equals(df_truth)
    # straight mutate
    t = df >> mutate(m=mean(X.x))
    df_truth = df.copy()
    df_truth['m'] = df_truth.x.mean()
    assert t.equals(df_truth)
    # grouped mutate
    t = df >> groupby(X.cut) >> mutate(m=mean(X.x))
    df_truth['m'] = pd.Series([3.950, 4.045, 4.195, 4.045, 4.195])
    assert t.equals(df_truth)


def test_first():
    df = diamonds >> select(X.cut, X.x) >> head(5)
    # straight summarize
    t = df >> summarize(f=first(X.x))
    df_truth = pd.DataFrame({'f': [3.95]})
    assert t.equals(df_truth)
    # grouped summarize
    t = df >> groupby(X.cut) >> summarize(f=first(X.x))
    df_truth = pd.DataFrame({'cut': ['Good', 'Ideal', 'Premium'],
                             'f': [4.05, 3.95, 3.89]})
    assert t.equals(df_truth)
    # straight mutate
    t = df >> mutate(f=first(X.x))
    df_truth = df.copy()
    df_truth['f'] = df_truth.x.iloc[0]
    assert t.equals(df_truth)
    # grouped mutate
    t = df >> groupby(X.cut) >> mutate(f=first(X.x))
    df_truth['f'] = pd.Series([3.95, 3.89, 4.05, 3.89, 4.05])
    assert t.equals(df_truth)


def test_last():
    df = diamonds >> select(X.cut, X.x) >> head(5)
    # straight summarize
    t = df >> summarize(l=last(X.x))
    df_truth = pd.DataFrame({'l': [4.34]})
    assert t.equals(df_truth)
    # grouped summarize
    t = df >> groupby(X.cut) >> summarize(l=last(X.x))
    df_truth = pd.DataFrame({'cut': ['Good', 'Ideal', 'Premium'],
                             'f': [4.34, 3.95, 4.20]})
    assert t.equals(df_truth)
    # straight mutate
    t = df >> mutate(l=last(X.x))
    df_truth = df.copy()
    df_truth['l'] = df_truth.x.iloc[4]
    assert t.equals(df_truth)
    # grouped mutate
    t = df >> groupby(X.cut) >> mutate(l=last(X.x))
    df_truth['l'] = pd.Series([3.95, 4.20, 4.34, 4.20, 4.34])
    assert t.equals(df_truth)


def test_n():
    df = diamonds >> select(X.cut, X.x) >> head(5)
    # straight summarize
    t = df >> summarize(n=n(X.x))
    df_truth = pd.DataFrame({'n': [5]})
    assert t.equals(df_truth)
    # grouped summarize
    t = df >> groupby(X.cut) >> summarize(n=n(X.x))
    df_truth = pd.DataFrame({'cut': ['Good', 'Ideal', 'Premium'],
                             'n': [2, 1, 2]})
    assert t.equals(df_truth)
    # straight mutate
    t = df >> mutate(n=n(X.x))
    df_truth = df.copy()
    df_truth['n'] = 5
    assert t.equals(df_truth)
    # grouped mutate
    t = df >> groupby(X.cut) >> mutate(n=n(X.x))
    df_truth['n'] = pd.Series([1, 2, 2, 2, 2, 2])
    assert t.equals(df_truth)