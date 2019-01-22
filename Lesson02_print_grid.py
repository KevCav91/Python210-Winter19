#----------------------------------------#
# Title: Lesson02_print_grid.py
# Initial File
# Claire Yoon,2019-01-12,New file
#----------------------------------------#

#print_grid function
def print_grid(grid,size):
    for g in range(grid):
        # horizontal grid - iterate for (grid) times
        for g in range(grid):
            print('+ ',end='')
            # horizontal grid - with size of (size)
            for s in range(size):
                print('- ',end='')
        print('+ ', end='')
        print()
        # vertical grid - iterate for (grid) times
        for s in range(size):
            print('| ',end='')
            for g in range(grid):
                # vertical grid - with size of (size)
                for s in range(size):
                    print('  ', end='')
                print('| ', end='')
            print()
    # horizontal grid - closing row
    for g in range(grid):
        print('+ ', end='')
        for s in range(size):
            print('- ', end='')
    print('+ ', end='')
    print()


print_grid(5,3)