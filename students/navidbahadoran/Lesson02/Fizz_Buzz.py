"""
title: Fizz_Buzz
Desc: for the number in the range of 1 to n:
      print “Fizz” instead of the number for multiples of three
      print “Buzz” instead of the number for the multiples of five .
      For numbers which are multiples of both three and five print “FizzBuzz” instead.
change log:
NBahadoran, 1/20/2018, Created Fizz_Buzz.py
"""

def fizz_buzz(n):
    """
    for the number in the range of 1 to n:
    print “Fizz” instead of the number for multiples of three
    print “Buzz” instead of the number for the multiples of five .
    For numbers which are multiples of both three and five print “FizzBuzz” instead.
    else print number.
    :param n: the input from user that need to be printed
    :return:
    """
    for num in range(1,n+1):

        if (num % 3 == 0) and (num % 5 == 0):
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


