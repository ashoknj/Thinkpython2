import math
"""
###########              Classes and Objects
A programmer-defined type is also called a class. A class definition looks like this:
    class Point:
        "Represents a point in 2-D space."   # This is the docString that explain what this class is for

    Defining a class named Point creates a class object:
    >>> Point
    <class '__main__.Point'>
    Because Point is defined at the top level, its “full name” is __main__.Point.

#### Object of a class
    The class object is like a factory for creating objects. To create a Point, you call Point as
    if it were a function:
        >>> blank = Point()
        >>> blank
        <__main__.Point object at 0xb7e9d3ac>

    The return value is a reference to a Point object, which we assign to blank.
    Creating a new object is called instantiation, and the object is an instance of the class.
    When you print an instance, Python tells you what class it belongs to and where it is
    stored in memory (the prefix 0x means that the following number is in hexadecimal).
#### Attributes
    You can assign values to an instance using dot notation: here x and y are the attributes
    >>> blank.x = 3.0
    >>> blank.y = 4.0

#### embedded object
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()  ##cornr attributes assignd as point object.
box.corner.x = 0.0 ## it can access x and y of Point object
box.corner.y = 0.0

#### Instances as Return Values
    Functions can return instances. For example, find_center takes a Rectangle as an
    argument and returns a Point that contains the coordinates of the center of the Rectangle:
    def find_center(rect):
        p = Point()
        p.x = rect.corner.x + rect.width/2
        p.y = rect.corner.y + rect.height/2
    return p

    Here is an example that passes box as an argument and assigns the resulting Point to
    center:
        >>> center = find_center(box)
        >>> print_point(center)
        (50, 100)
####  Objects Are Mutable
    You can change the state of an object by making an assignment to one of its attributes. For
    example, to change the size of a rectangle without changing its position, you can modify
    the values of width and height:
        box.width = box.width + 50
        box.height = box.height + 100

        def grow_rectangle(rect, dwidth, dheight):
            rect.width += dwidth
            rect.height += dheight
    Here is an example that demonstrates the effect:
        >>> box.width, box.height
        (150.0, 300.0)
        >>> grow_rectangle(box, 50, 100)
        >>> box.width, box.height
        (200.0, 400.0)
    Inside the function, rect is an alias for box, so when the function modifies rect, box
    changes.
#### Copying
    The copy module contains a function called copy that can duplicate any object:
    >>> p1 = Point()
    >>> p1.x = 3.0
    >>> p1.y = 4.0
    >>> import copy
    >>> p2 = copy.copy(p1)
    p1 and p2 contain the same data, but they are not the same Point:
    >>> print_point(p1)
    (3, 4)
    >>> print_point(p2)
    (3, 4)
    >>> p1 is p2
    False
    >>> p1 == p2  
    False

    If you use copy.copy to duplicate a Rectangle, you will find that it copies the Rectangle
    object but not the embedded Point:
    >>> box2 = copy.copy(box)
    >>> box2 is box
    False
    >>> box2.corner is box.corner
    True   ##Refer to below notes why it returned True

    it checks object identity, not object equivalence. That’s because for programmer-defined types, Python doesn’t know
    what should be considered equivalent. 
    This operation is called a shallow
    copy because it copies the object and any references it contains, but not the embedded
    objects.
####  Deep Copy
    the copy module provides a method named deepcopy that copies not only the
    object but also the objects it refers to, and the objects they refer to, and so on. this operation is called a deep copy

    >>> box3 = copy.deepcopy(box)
    >>> box3 is box
    False
    >>> box3.corner is box.corner
    False
#### DEbugging  use the functions like isinstance(), hasattr(), Try except block
    If you try to access an attribute that doesn’t exist, you get an AttributeError:
        >>> p = Point()
        >>> p.x = 3
        >>> p.y = 4
        >>> p.z
        AttributeError: Point instance has no attribute 'z'

    You can also use isinstance to check whether an object is an instance of a class:
        >>> isinstance(p, Point)
        True
    If you are not sure whether an object has a particular attribute, you can use the built-in
        function hasattr:
        >>> hasattr(p, 'x')
        True
        >>> hasattr(p, 'z')
        False

    You can also use a try statement to see if the object has the attributes you need:
        try:
            x = p.x
        except AttributeError:
            x = 0

"""

class Point:
        """
        Represents a point in 2-D space.   

        """
def distance_between_points(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

    #return p2.x-p1.x,p2.y-p1.y


print(Point)  #<class '__main__.Point'>
p=Point()
print(p) #<__main__.Point object at 0x000001A8F2D49700>
p1=Point()
p1.x=10
p1.y=20
p2=Point()
p2.x=25
p2.y=50
print(distance_between_points(p1,p2))
