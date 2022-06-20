from tkinter import N
import turtle,math

bob=turtle.Turtle()
# bob.pendown()
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)  #fd,bk,lt,rt  are for morward, backward, right, left
# bob.lt(90)
# bob.fd(100)  #fd,bk,lt,rt  are for morward, backward, right, left
# bob.lt(90)
# bob.fd(100)  #fd,bk,lt,rt  are for morward, backward, right, left

#### draw square uisng a for loop

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)
#print(bob)
#turtle.mainloop()
#input("press any key to exit")  #To keep the window open

##### Example 1 page    75

# def draw_square(t,l):
#     for i in range(4):
#         t.fd(l)
#         t.lt(90)
# def polygon(t,l,n):
#     angle=360/n
#     for i in range(n):
#         t.fd(l)
#         t.lt(angle)

# def circle(t,r):
#     cm=2*math.pi*r
#     n=50
#     length=cm/n
#     polygon(t,length,n)

#draw_square(bob,200)
#polygon(bob,10,100)
#circle(bob,30)
#print(bob)
#input("press any key to exit")  #To keep the window open

#### encapsulation (EX: above draw_square())
# Wrapping a piece of code up in a function is called encapsulation. One of the benefits of
# encapsulation is that it attaches a name to the code, which serves as a kind of
# documentation. Another advantage is that if you reuse the code, it is more concise to call a
# function twice than to copy and paste the body!

##### Generalization
# Adding a parameter to a function is called generalization because it makes the function
# more general: in the previous version, the square is always the same size; in this version it
# can be any size.

##### interface  (Ex: above Circle function)
# The interface of a function is a summary of how it is used: what are the parameters? What
# does the function do? And what is the return value? An interface is “clean” if it allows the
# caller to do what they want without dealing with unnecessary details.

###### Refactoring
# This process — rearranging a program to improve interfaces and facilitate code reuse — is
# called refactoring. In this case, we noticed that there was similar code in arc and
# polygon, so we “factored it out” into polyline.
#### DocString  
# it's like the notes/commens written in between two set of 3 double quotes  
def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
angle (in degrees) between them. t is a turtle.
"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)
circle(bob,30)
print(bob)
#input("press any key to exit")  #To keep the window open
