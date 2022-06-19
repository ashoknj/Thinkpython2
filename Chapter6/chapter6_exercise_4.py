"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function
called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case.
"""
def a_poower(a,b):
    if a<b:
        return False
    if a==b:
        return True
    if a%b==0:
        c=a/b
        return a_poower(c,b)
    else:
        return False

#print(12%5)
print(a_poower(1,2))
