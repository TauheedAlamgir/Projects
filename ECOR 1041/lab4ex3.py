#Tauheed Alamgir 101194927

import math
def distance(x1: float, y1: float, x2: float, y2: float):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
def area_of_disk(radius: float):
    return math.pi * radius ** 2
def area_of_circle(xc: float, yc: float, xp: float, yp: float):
    """
    Returns the area of a circle using th distance formula to find the radius
    then it uses pi*r^2
    >>> are = area_of_circle(1,2,3,4)
    25.132741228718352
    >>> are = area_of_circle(7,6,8,5)
    6.283185307179588
    >>> are = area_of_circle(5,6,12,45)
    4932.3004661359755
    """
    return math.pi * (distance(xc, yc, xp, yp)) ** 2

are = area_of_circle(1,2,3,4)
print(are)
are = area_of_circle(7,6,8,5)
print(are)
are = area_of_circle(5,6,12,45)
print(are)
