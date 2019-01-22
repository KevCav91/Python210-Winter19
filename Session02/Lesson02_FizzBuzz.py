#----------------------------------------#
# Title: Lesson02_FizzBuzz.py
# Initial File
# Claire Yoon,2019-01-12,New file
#----------------------------------------#

for i in range(1,101):
    # in case of multiple of 15
    if i % 15 == 0:
        print("FizzBuzz")
    # in case of multiple of 3
    elif i % 3 == 0:
        print("Fizz")
    # in case of multiple of 5
    elif i % 5 == 0:
        print("Buzz")
    # other than that, print itself
    else:
        print(i)
