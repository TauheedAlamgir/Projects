# Tauheed Alamgir 101194927

def middle_way(t: list, a:list) -> str:
    """
    Returns the digit in the middle of both lists as a new list
    >>> middle_way([1, 2, 3], [4, 5, 6])
    [2, 5]
    >>> middle_way([234, 671, 893], [649, 193, 974])
    [671, 193]
    >>> middle_way([99, 45, 56], [12, 34, 38])
    [45, 34]
    """
    return [t [1], a [1]]

x = [1, 2, 3]
y = [4, 5, 6]
print(middle_way(x, y))
x = [234, 671, 893]
y = [649, 193, 974]
print(middle_way(x, y))
x = [99, 45, 56]
y = [12, 34, 38]
print(middle_way(x, y))