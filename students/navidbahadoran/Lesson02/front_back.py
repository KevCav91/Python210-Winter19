"""
title: front_back
change log:
NBahadoran, 1/19/2018,Created front_back.py
"""
def front_back(str):
    """
    Given a string, return a new string where the first and last chars have been exchanged.
    front_back('code') → 'eodc'
    front_back('a') → 'a'
    front_back('ab') → 'ba'
    """
    if len(str)<=1: return str
    return str[-1]+str[1:len(str)-1]+str[0]

