from __future__ import print_function, division

import copy

from practice_example import Point, Rectangle, print_point
from Chapter15_Practice import distance_between_points

"""
Write a definition for a class named Circle with attributes center and radius, where
center is a Point object and radius is a number.
Instantiate a Circle object that represents a circle with its center at and
radius 75.
Write a function named point_in_circle that takes a Circle and a Point and returns True
if the Point lies in or on the boundary of the circle.
Write a function named rect_in_circle that takes a Circle and a Rectangle and returns
True if the Rectangle lies entirely in or on the boundary of the circle.
Write a function named rect_circle_overlap that takes a Circle and a Rectangle and
returns True if any of the corners of the Rectangle fall inside the circle. Or as a more
challenging version, return True if any part of the Rectangle falls inside the circle.

"""
"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""



class Circle:
    """Represents a circle.
    Attributes: center, radius
    """


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).
    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()