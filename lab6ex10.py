# Tauheed Alamgir 101194927

def reverse(t: list) -> list:
    """
    Return the list in reverse order
    >>> reverse([10,9,8,7,6,5,4,3,2,1,0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> reverse([7,3,9,1,7,3,5,2,3,90])
    [90, 3, 2, 5, 3, 7, 1, 9, 3, 7]
    >>> reverse([99,88,77,1,2,3])
    [3, 2, 1, 77, 88, 99]
    """
    total = [0] * len(t)
    for a in range(len(t)):
        total [len(t) - a - 1] = t[a]
    return total

lst = [10,9,8,7,6,5,4,3,2,1,0]
print(reverse(lst))
lst = [7,3,9,1,7,3,5,2,3,90]
print(reverse(lst))
lst = [99,88,77,1,2,3]
print(reverse(lst))

