# Tauheed Alamgir 101194927

def make_ends(end: list) -> str:
    """
    Returns a new list consisting of the first and last digit of the list given
    >>> make_ends([1, 2, 3, 4])
    [1, 4]
    >>> make_ends([4, 5, 6, 7])
    [4, 7]
    >>> make_ends(9, 10, 11, 12, 13)
    [9, 13]
    """
    return [end [0], end[len(end) - 1]]

x = [1, 2, 3, 4]
print(make_ends(x))
x = [4, 5, 6, 7]
print(make_ends(x))
x = [9, 10, 11, 12, 13]
print(make_ends(x))