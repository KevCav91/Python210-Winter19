"""
title: Fibonacci and lucas series
Desc: for the number n it returns the nth elements of fibonacci and lucas series
change log:
NBahadoran, 1/20/2018, Created series.py
"""
def fibonacci(n):
    """
    The function should return the nth value in the fibonacci series (starting with zero index).
    :param n: the number of element in the series
    :return:nth value of fibonacci series
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """
    The function should return the nth value in the lucas series (starting with zero index).
    :param n: the number of element in the series
    :return: nth value of lucas series
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n,first_element=0,second_element=1):
    """
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    :param n: the number of element in the series
    :param first_element: determine the first element of the series
    :param second_element: determine the second element of the series
    :return: nth value of series which is the adding of n-1th and n-2th elements.
    """
    if n == 0:
        return first_element
    elif n == 1:
        return second_element
    else:
        return sum_series(n - 1,first_element,second_element) + sum_series(n - 2,first_element,second_element)

try:
    number=int(input("Enter the integer No of element of the fibonacci and lucas that you want to print:"))

    print(fibonacci(number))
    print(lucas(number))

    first_element=int(input("Enter the value of the first element of series:"))
    second_element = int(input("Enter the value of the second element of series:"))

    print(sum_series(number,first_element,second_element))

    """Block of test: in this test we check if our functions generate the 
    right numbers
    """
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7
    # test if sum_series matched fibonacci
    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")

except AssertionError as e:
    print("test is not passed",e)

except Exception:
    print("You entered the wrong input!")
    print("Your input should  be integer.")

