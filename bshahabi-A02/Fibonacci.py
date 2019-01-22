#--------------------------#
#Title: This script computes fibonacci series"
# Change log (Who,When,What)
#bshahabi,1/20/2019,Created the file"

def fib(n):
 a = 0
 b = 1
 for i in range(n):
    print(a)
    c = a
    a = b
    b = c + b


def lucas(n):
 a = 2
 b = 1
 for i in range(n):
    print(a)
    c = a
    a = b
    b = c + b

#The following function can calculate both Fibonacci and Lucas series
def sum_series():
    n = int(input("Enter the desired range for the Fib/Lucas series:"))
    selectFun = int(input("Enter number 1 for the Fib and 2 for Lucas series:"))

    if selectFun==2:
        lucas(n)
    elif selectFun==1:
        fib(n)
    else:
        print("An invalid number entered!")


sum_series()