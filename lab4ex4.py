#Tauheed Alamgir 101194927

import math
def height(length: float, angle: float):
    """
    Returns the height reached by the ladder given the length of the ladder 
    and the angle at which it sits
    hei = height(12,13)
    2.69941265212638
    hei = height(11.9,32.8)
    6.446327702364603
    hei = height(3,68.9)
    2.798860604476467
    """
    return math.sin(angle * math.pi / 180) * length

hei = height(12,13)
print(hei)
hei = height(11.9,32.8)
print(hei)
hei = height(3,68.9)
print(hei)
