# Tauheed Alamgir 101194927

def divisors(t: int) -> list: 
    """
    Returns a new list of the divisors of our input digit
    >>> divisors(9)
    [1, 3, 9]
    >>> divisors(67)
    [1, 67]
    >>> divisors(1000)
    [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]
    """
    a = []
    for x in range(1, t):
        if t % x == 0:
            a += [x]
    return a + [t]

lst = 9
print(divisors(lst))
lst = 67
print(divisors(lst))
lst = 1000
print(divisors(lst))
