#####################################
#TITLE: Lab 1-1
#Change Log: (Who, When, What)
#JJameson, 01 12 2019: created File
####################################

#Defining functions
def causeNameErrorException ():
    #raise NameError("Error") the name error will raise an exception because the name 'nameNotFound' does not exist.
    print(nameNotFound)


def causeTypeError ():
    #raise TypeError() the type error will raise an exception because I am mixing intigers and strings.
    print ('yes' + 6)

def causeSyntaxError():
    # raise SyntaxError() the syntax error will raise an exception because I did not include parenthesis in my print\
    # statement.
    #print "I forgot the parenthesis"

def caauseAttributeError():# raise AttributeError() the attribute error will raise an exception because I did not define the attribuete 'broken' print.broken


# Calling the functions.
#causeNameErrorException()
#causeTypeError()
#causeSyntaxError()
causeAttributeError()
