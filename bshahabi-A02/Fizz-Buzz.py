#--------------------------#
#Title: This script is supposed to find the multiples of 3 and 5 in the range of (1,100)"
# Change log (Who,When,What)
#bshahabi,1/20/2019,Created the file"

def multiple_finder():

    for num in range(1,101):
      if(num % 3 == 0 and num % 5 == 0):
        print('FizzBuzz')
      if num % 3 == 0:
        print('Fizz')
      elif num % 5 == 0:
        print('Buzz')
      else:
        print(num)


multiple_finder()