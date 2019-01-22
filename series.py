#----------------------------------------#
# Title: series.py
# Initial File
# Claire Yoon,2019-01-12,New file
#----------------------------------------#

# fibaonacci function - based on recursion
def fibonacci(n):
    # set base case
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Lucas function - also based on recursion
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

# using recursion more generically
def sum_series(n, n0=0, n1=1):
    #  without optional parameters, identical with fibonacci
    if(n0 is None and n1 is None):
        return fibonacci(n)
    # same formula with Lucas but calculating with optional initial values
    elif(n0 is not None or n1 is not None):
        if n == 0:
            return n0
        elif n == 1:
            return n1
        return sum_series(n-1,n0,n1) + sum_series(n-2,n0,n1)


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

