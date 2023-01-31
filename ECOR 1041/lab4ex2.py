#Tauheed Alamgir 101194927

import math
def distance(x1: float, y1: float, x2: float, y2: float):
    """
    Returns the distance between 2 points given (x1,x2,y1,y2)
    >>> dis = distance(1,2,3,4)
    2.8284271247461903
    >>> dis = distance(4,21,3,8)
    13.038404810405298
    >>> dis = distance(11,3,6,12)
    10.295630140987
    >>> dis = distance(7,6,9,10)
    4.47213595499958
    """
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

dis = distance(1,2,3,4)
print(dis)
dis = distance(4,21,3,8)
print(dis)
dis = distance(11,3,6,12)
print(dis)
dis = distance(7,6,9,10)
print(dis)
