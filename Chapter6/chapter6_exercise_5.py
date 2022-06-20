"""
The greatest common divisor (GCD) of a and b is the largest number that divides both of
them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the
remainder when a is divided by b, then . As a base case, we
can use .
Write a function called gcd that takes parameters a and b and returns their greatest
common divisor.
Credit: This exercise is based on an example from Abelson and Sussman’s Structure and
Interpretation of Computer Programs (MIT Press, 1996).
"""
"""  In correct one
def gcf(a,b):
    if a>b:
        return "No GCF"
    if b%a==0:     #assumption a is small number
        return a
    else:
        r=b%a
        r1=b%r
        r2=a%r
        if r1==0 and r2==0:    # for 12,42 the r is 6 and both 12 and 42 are divisible by 6
            return r
        if r1==r2:
            return r1          #for 12, 105
        else:
            num1=r1
            num2=r2
            if r1==0:
                num1=r
            if r2==0:
                num2=r
            if num1<num2:
                return gcf(num1,num2)
            else:
                return gcf(num2,num1)
            
            
       

print(gcf(9,24))  #3
print(gcf(12,105))  #3
print(gcf(6,32))  #3
print(gcf(16,52))  #3
print(gcf(24,55))  #3
"""

def gcf(a,b):
    if b==0:
        return abs(a)
    else:
        return gcf(b,a%b)

# Python code to demonstrate naive
# method to compute gcd ( Euclidean algo )
 
def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
a = 60
b = 48
 
# prints 12
#print ("The gcd of 60 and 48 is : ",end="")
#print (computeGCD(60, 48))
print (computeGCD(9, 24))
#print(gcf(9,24))  #3
#print(gcf(12,105))  #3
#print(gcf(6,32))  #2
#print(gcf(16,52))  #4
#print(gcf(24,55))  #1
#print(gcf(24,56))  #1

