# Tauheed Alamgir 101194927

def has22(t: list) -> bool:
    """
    Returns True if 2 is next to another 2 or returns False
    >>> has22([2,2,3,4,5])
    True
    >>> has22([9,8,7,6,5,4,3,2,1,0])
    False
    >>> has22([1,2,2,5,7,4,2])
    True
    """
    x = 0
    for x in range(len(t)):
        if t [x] == 2 and t [x - 1] == 2:
            return True
    return False

a = [2,2,3,4,5]
print(has22(a))
a = [9,8,7,6,5,4,3,2,1,0]
print(has22(a))
a = [1,2,2,5,7,4,2]
print(has22(a))
