#####  Functions
#It is common to say that a function “takes” an argument and “returns” a result. The result
#is also called the return value.
#A module is a file that contains a collection of related functions. EX: import math
#The module object contains the functions and variables defined in the module.  
# you can access then with Dot notation EX: math.pi, math.sqrt(25)

#Composition the argument of a function can be any kind of expression, including arithmetic operators
#EX: x = math.sin(degrees / 360.0 * 2 * math.pi)

## User defined functiona

# def is a keyword that indicates that this is a function definition
# The rules for function names are the same as for variable names: letters,
# numbers and underscore are legal, but the first character can’t be a number. You can’t use
# a keyword as the name of a function, and you should avoid having a variable and a
# function with the same name
# The first line of the function definition is called the header; the rest is called the body.
# The header has to end with a colon and the body has to be indented. By convention,
# indentation is always four spaces. The body can contain any number of statements.
#you can have nested function

## Flow of Execution
#Code inside the fucntion never execute until function is called
# when you read a program, you don’t always want to read from top to bottom.
# Sometimes it makes more sense if you follow the flow of execution.

## Function Parameters and Arguments
# fuction can accept multiple paramters. when the same fucntion is called we passed the arguments.
# Inside the function, the arguments are assigned to variables called parameters
#  EX: def printname(name):   here name is paramters
#           print(name)
#   printname("Robert Xi")  #here the string "Reboert Xi" is the argument 
# the variables and paramters inside the function  are local. can't be accessed from outisde of function

#When you create a variable outside of any function, it belongs to __main__.

#Stack diagram - shows the functions and all the variable values inside that
#If an error occurs during a function call, Python prints the name of the function, the name
#of the function that called it, and the name of the function that called that, all the way back
#to __main__. This list of functions is called a traceback.The order of the functions in the traceback is the same as the order of the frames in the
#stack diagram. The function that is currently running is at the bottom.
#------- Example

#Traceback (innermost last):
#File "test.py", line 13, in __main__
#cat_twice(line1, line2)
#File "test.py", line 5, in cat_twice
#print_twice(cat)
#File "test.py", line 9, in print_twice
#print(cat)
#NameError: name 'cat' is not defined

# Fruitful function returns value
#Void function doesn't return any value. If you assign the result to a variable, you get a special value
#called None:

import math
def showmath():
    print(math.pi)
    print(math.sqrt(25))
showmath()

def addnum(n1,n2):
    return n1+n2

print(addnum(12,13))


