# Tauheed Alamgir 101194927

def count_evens(t: list) -> int:
    """
    Returns the amount of even digits in our list
    >>> count_evens([1,2,3,4,5,6,7,8,9])
    4
    >>> count_evens([11,67,53,56,31,32])
    2
    >>> count_evens([-9,-2,2,4,6,7,5,91])
    4
    """
    x = 0
    for ele in t:
        if ele % 2 == 0:
            x += 1
    return x

t = [1,2,3,4,5,6,7,8,9]
print(count_evens(t))
t = [11,67,53,56,31,32]
print(count_evens(t))
t = [-9,-2,2,4,6,7,5,91]
print(count_evens(t))
