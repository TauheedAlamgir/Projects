# Tauheed Alamgir 101194927

def multiply_uniques(a: int, b:int , c:int) -> int:
    """
    Returns the product of all 3 digits if all 3 digits are different, but any 
    of the 3 digits are the same then it returns the odd number
    >>> mu = multiply_uniques(4,5,9)
    180
    >>> mu = multiply_uniques(3,2,3)
    2
    >>> mu = multiply_uniques(7,7,7)
    0
    >>> mu = multiply_uniques(9,9,12)
    12
    >>> mu = multiply_uniques(666,999,999)
    666
    """
    if (a == b) and (b == c) and (c == a):
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif (a != b) and (b != c) and (c != a):
        return (a) * (b) * (c)
    
mu = multiply_uniques(4,5,9)
print(mu)
mu = multiply_uniques(3,2,3)
print(mu)
mu = multiply_uniques(7,7,7)
print(mu)
mu = multiply_uniques(9,9,12)
print(mu)
mu = multiply_uniques(666,999,999)
print(mu)