######## Exercise 3.1
from operator import concat


def right_justify(name):
    totalspace=70-len(name)
    finalname=""
    
    while totalspace>0:
        finalname=concat(finalname," ")
        totalspace=totalspace-1
    print(concat(finalname,name))
#right_justify("ashok khandelwal")

##### Exercise 3.2
# def do_twice(f,msg):
#     f(msg)
#     f(msg)

# def do_four(f,msg):
#     do_twice(f,msg)
#     do_twice(f,msg)

# do_twice(print,"hello")
# print('')
# do_four(print,"Hi")

##### Exercise 3.3   print grid
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
    
print("By Ashok Khandelwal", end=' ')  ##end keyword will not end with a new line
print("date: 06-10-2022")
