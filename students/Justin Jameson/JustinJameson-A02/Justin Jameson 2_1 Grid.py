# **************************
# Title: Grid Maker
# Desc: creates a grid based on user input.
# Change Log:
# Justin Jameson, 01/17/2019, version 1
# **************************


# -- Data --#
# declare variables and constants
intCounter = 0
# intCounter is used in the while loop to create the rows.
# rowWidth = the graphics formula for printing the top and bottom row of the grid.
# rowHeight = the graphics formula for printing the sides of the grid.
# gx is user input that defines the width of the cells.
# gy is user input that defines the height of the cells.
# nColumns is user input that defines how many Columns to print.
# nRows is user input that defines how many rows to print.

# -- Processing -- #


def GridGraphics(gx, gy, nColumns):
    """
    :param gx: defines width of the row
    :param gy: defines height of the row
    :param nColumns: defines the number of Columns
    :return: returns gx-1 dashes and gy-2
    """
    rowWidth = ("+"+(gx * " - ")+"+")+(((gx * " - ")+"+")* (nColumns - 1))
    rowHeight = (("|"+(gx*"   ") + "|") + (((gx*"   ") + "|")* (nColumns - 1)) + "\n")* gy
    return rowWidth, rowHeight
# end function GridGraphics


# -- Presentation (Input/Output) --#

# get user input
# user defines height and width of the cell(s).
print("First, lets define the cell size. ")
cellWidth = int(input("Enter the width of the cell: "))
cellHeight = int(input("Enter the height of the cell: "))
print("Now lets define the grid. ")
numberColumns = int(input("Enter the number of columns: "))
nRows = int(input("Enter the number of row: "))

# Send program output, printing out the grids.
while intCounter < nRows:
    rW, rH = GridGraphics(cellWidth, cellHeight, numberColumns)
    print(rW + "\n" + rH, end="")
    intCounter = intCounter + 1
# End of while loop
# Print out the final set of + -
print(rW)



