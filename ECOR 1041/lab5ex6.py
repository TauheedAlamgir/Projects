# Tauheed Alamgir 101194927

def great_42(x: int, y: int) -> bool:
    """
    It takes two values a and b  and returns True if either value is 42 or if 
    their sum or the absolute value of the difference is 42
    >>> gr = great_42(9, 33)
    True
    >>> gr = great_42(4, 7)
    False
    >>> gr = great_42(-40,46)
    False
    >>> gr = great_42(56,14)
    True
    """
    if abs(x) == 42:
        return True
    elif abs(y) == 42:
        return True
    elif abs(x + y) == 42:
        return True
    elif abs(x - y) == 42:
        return True
    return False

gr = great_42(9, 33)
print(gr)
gr = great_42(4, 7)
print(gr)
gr = great_42(-40,46)
print(gr)
gr = great_42(56,14)
print(gr)
