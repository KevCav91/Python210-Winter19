"""
title: Sum_double
change log:
NBahadoran, 1/13/2018, Created sum_double.py
"""

def sum_double(a, b):
    """
    Given two int values, return their sum.
    Unless the two values are the same, then return double their sum.
    sum_double(1, 2) → 3
    sum_double(3, 2) → 5
    sum_double(2, 2) → 8
    """
    return(a+b if a!=b else (a+b)*2)

print(sum_double(1,1))
print(sum_double(1,2))
#