# Tauheed Alamgir 101194927

def common_end(t: list, a: list) -> bool:
    """
    Returns True if the first or the last digit of the lists are the same and 
    returns True if the the first and last digit of both lists are the same
    returns False if the the first and/or last digits are not thr same
    >>> common_end([1, 2, 3, 4], [3, 6, 4, 4])
    True
    >>> common_end([6, 7, 8, 19], [6, 8, 61, 18])
    True
    >>> common_end([13, 98, 63, 13], [60, 37, 32, 60])
    True
    >>> common_end([1,2,3,4], [5,6,7,8])
    False
    """
    if (t[0] == a[0]) or (t[-1] == a[-1]):
        return True
    elif (t[0] == t[-1]) and (a[0] == a[-1]):
        return True
    return False

x = [1, 2, 3, 4]
y = [3, 6, 4, 4]
print(common_end(x, y))
x = [6, 7, 8, 19]
y = [6, 8, 61, 18]
print(common_end(x, y))
x = [13, 98, 63, 13]
y = [60, 37, 32, 60]
print(common_end(x, y))
x = [1,2,3,4]
y = [5,6,7,8]
print(common_end(x, y))
