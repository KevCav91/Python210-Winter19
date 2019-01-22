"""
title: makes10
change log:
NBahadoran, 1/19/2018, Created makes10.py
"""

def makes10(a, b):
    """
    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


    makes10(9, 10) → True
    makes10(9, 9) → False
    makes10(1, 9) → True
    """
    return (a + b == 10 or a == 10 or b == 10)
