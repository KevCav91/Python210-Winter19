# -------------------------------------------- #
# Title: Lesson 02 Exercise: Fibonacci Series
# Desc: Holds functions (and asset tests) related to the Fibonacci and Lucas series
# Change log: (who, when, what)
# RKesterson, 2019-01-22, Created file
# RKestesron, 2019-01-22, Stubbed out methods / parts
# RKesterson, 2019-01-22, Completed step one (fibonacci function)
# RKesterson, 2019-01-22, Completed step two (lucas function)
# RKesterson, 2019-01-22, Completed step three (sum_series function)
# RKesterson, 2019-01-22, Completed testing using assert statements
# ---------------------------------------------- #

# Define the function
def fibonacci(n):
    """ compute the nth Fibonacci number """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

# Call the function
print(fibonacci(7))

'''
def lucas(n):
    """ compute the nth Lucas number """
    pass


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    pass



if __name__ == "__main__":
    # run some tests
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

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
'''