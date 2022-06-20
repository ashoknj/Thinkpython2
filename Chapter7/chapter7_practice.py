import math
import sys
##While statement simple recursion
def countdown(n):
    #while n>0:
    while(n):  ## this also run while n is zero
        print(n)
        n=n-1
    print("BLASTOFF!!!")

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0: # n is even
            n = n / 2
        else: # n is odd
            n = n*3 + 1
def testbreak():    ## keep asking for user input until user type done. 
    while True:
        line=input(">")
        if line=="done":
            break
        print(line)
    print("Done!!!!")
def squareroot(num,guess):  ##use newton's formula to calculate square root
        while True:
            #print(num)
            y=(guess+(num/guess))/2
            if y==num:
                break
            if abs(y-guess)<sys.float_info.epsilon:
                break
            num=y
        return y
"""
Algorithms
Newton’s method is an example of an algorithm: it is a mechanical process for solving a
category of problems (in this case, computing square roots).
Executing algorithms is boring, but designing them is interesting, intellectually
challenging, and a central part of computer science
"""

#countdown(10)
#sequence(10)
#testbreak()
print(squareroot(25,5))
