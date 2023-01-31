# Tauheed Alamgir 101194927

def bakers_party(p: int, h: bool) -> bool:
    """
    Returns if the party has been succesful according to pastries sold and if it
    was a holiday or weekday
    >>> bake = bakers_party(51, True)
    True
    >>> bake = bakers_party(21, False)
    False
    >>> bake = bakers_party(68, False)
    False
    """
    a = 40
    b = 60
    if (p >= a) and (p <= b):
        return True
    elif (p >= a) and h:
        return True
    return False

bake = bakers_party(51, True)
print(bake)
bake = bakers_party(21, False)
print(bake)
bake = bakers_party(68, False)
print(bake)