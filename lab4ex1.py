#Tauheed Alamgir 101194927

import math
def area_of_disk(radius: float):
 """
 Returns the area of a disk given the radius
 >>> area = area_of_disk(5)
 78.53981633974483
 >>> area = area_of_disk(5.0)
 78.53981633974483
 >>> area = area_of_disk(9.0)
 254.46900494077323
 >>> area = area_of_disk(11)
 380.132711084365
 """
 return math.pi * radius ** 2

area = area_of_disk(5)
print(area)
area = area_of_disk(5.0)
print(area)
area = area_of_disk(9.0)
print(area)
area = area_of_disk(11)
print(area)