#------------------------------------#
# Title: FizzBuzz
# Desc: This program writes "fiz for multiples of 3 and buzz for multiples of 5
# Change Log: (Who, When, What)
# Kim Voros, 1/21/2019, Wrote program
# ------------------------------------#

# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

# -- Data --#

#Create variable containers for 3, 5 and counter, set to 0

cal3 = 0
cal5 = 0
couter = 0


# -- Processing --#

#write function to count 0 - 100 and print results

def cal():
    # create range statement that increases by 1
    for cal in range(101):
        cal = cal
# calculate remainders
        cal3 = cal % 3
        cal5 = cal % 5
# print results
        if cal3 == 0 and cal5 != 0:
            print('fiz')
        elif cal5 != 0 and cal5 == 0:
            print('buzz')
        elif cal3 == 0 and cal5 == 0:
            print('fizzbuzz')
        else:
            print('cal = {},'.format(cal) )

cal()


