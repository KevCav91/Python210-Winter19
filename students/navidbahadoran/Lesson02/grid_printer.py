"""
title: grid_printer
Desc: print a grid with the same row and column number and each cell has the
    size based on the user's input for the size
change log:
NBahadoran, 1/20/2018, Created grid_printer.py
"""

def grid(row,size):
    """
    print the grid based on the size and the row input
    :param row: No of row and column of the grid
    :param size: size of each cells
    :return: print the grid
    """
    print_row(row, size)

    for grid_row in range(row):

        for cell_size in range(size):
            print_beam(row,size)

        print_row(row, size)



def print_beam(row,size):
    """
    print the beam of the grid
    :param row: No of | in the row minus 1
    :param size: half of No of blank in the row
    :return: print row which includes beams
    """
    post = "|"
    blank = " "
    for i in range(row):
        print(post, end=blank)
        for j in range(size):
            print(blank + blank, end="")
    else:
        print(post)

def print_row(row,size):
    """
    print the row of the grid
    :param row: No of + in the row minus 1
    :param size: half of No of - in the row
    :return: print row which includes + -
    """
    plus = "+"
    blank= " "
    minus= "-"
    for i in range(row):
        print(plus, end=blank)
        for j in range(size):
            print(minus + blank, end="")
    else:
        print(plus)

try:
    row=int(input("Enter the integer No of row of your grid: "))
    size=int(input("Enter the integer No of size of your grid: "))
    grid(row,size)
except Exception:
    print("You entered the wrong input!")
    print("Your input should  be integer.")

