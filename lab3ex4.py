#Tauheed Alamgir 101194927

import math
def area_of_cone(height, radius):
 return math.pi * radius * (math.sqrt(radius ** 2) + (height ** 2))

area = area_of_cone(3.0, 11)
print(area)
area = area_of_cone(0.0, 7.0)
print(area)
area = area_of_cone(9.0, 0)
print(area)
area = area_of_cone(4.0, 5.0)
print(area)