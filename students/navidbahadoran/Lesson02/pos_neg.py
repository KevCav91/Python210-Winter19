"""
title: pos_neg
change log:
NBahadoran, 1/19/2018, Created pos_neg.py
"""
def pos_neg(a, b, negative):
    """
    Given 2 int values, return True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only if both are negative.
    pos_neg(1, -1, False) → True
    pos_neg(-1, 1, False) → True
    pos_neg(-4, -5, True) → True
    """
    if negative:
        return (a<0 and b<0)
    else:
        return (a*b<0)
    return False
