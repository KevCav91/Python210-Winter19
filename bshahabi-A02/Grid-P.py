#--------------------------#
#Title: This script prints a Grid"
# Change log (Who,When,What)
#bshahabi,1/20/2019,Created the file"


def abc(rc, cell):
        #for i in range(rc):
            #Create vertical sqr
            for j in range(rc):
                #First row of the sqr
                print('+', end=' ')
                for x in range(cell):
                    print('-', end=' ')
                print('+')
                #Middle rows of the sqr
                for x in range(cell):
                    print('|', end=' ')
                    for x in range(cell):
                        print(' ', end=' ')
                    print('|')
            #Last row of the sqr
            print('+', end=' ')
            for x in range(cell):
                print('-', end=' ')
            print('+')


#Change the Grid size usign the following values:

abc(2, 3)