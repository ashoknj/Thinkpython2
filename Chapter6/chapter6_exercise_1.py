def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))

""""Stack diagram
C(1,5,3)
in C
total=9
    b(9)=90
        prod=a(9,9)=90
            
square=90**2=8100
"""


