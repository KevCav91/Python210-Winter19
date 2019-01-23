"""
title: def_21
change log:
NBahadoran, 1/13/2018, Created def_21.py
"""
def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, 
    except return double the absolute difference if n is over 21.
    diff21(19) → 2
    diff21(10) → 11
    diff21(21) → 0
    """
    return(abs(n-21) if n<21 else 2*abs(n-21))


print(diff21(23))