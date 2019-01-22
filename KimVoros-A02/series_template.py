#------------------------------------#
# Title: Series
# Desc: This is the solution set for the series template
# Change Log: (Who, When, What)
# Kim Voros, 1/21/2019, Wrote program
# ------------------------------------#
"""
a template for the series assignment
"""
# Python program to display the Fibonacci sequence up to n-th term using recursive functions
def fibonacci(n):
    """ compute the nth Fibonacci number """
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

# Change this value for a different result
nthNumber = 10

# check if the number of terms is valid
if nthNumber <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nthNumber):
       print(fibonacci(i))


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
