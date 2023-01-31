# Tauheed Alamgir 101194927

# EX 1
def bakers_party(p: int, holi: bool) -> bool:
    """
    Returns False if it is a weekday and True if its weekend
    number of pastries between 40 and 60 its a weekday if over 60 then its the
    weekend.
    >>> bakers_party(54, False)
    True
    >>> bakers_party(100, False)
    False
    >>> bakers_party(99, True)
    True
    """
    n = 40
    k = 60
    if p >= n and p <= k:
        return True
    elif p >= n and holi:
        return True
    return False


# EX 2
def squirrel_play(p: int, n: bool) -> bool:
    """
    Returns False for squirrels playing if temperature is between 90 and 100
    and True if its between 60 and 90 and squirrels play outside.
    >>> squirrel_play(89, False)
    True
    >>> squirrel_play(91, False)
    False
    >>> squirrel_play(89, True)
    True
    """
    if p >= 60 and p <= 90:
        return True
    elif p >= 60 and p <= 100 and n:
        return True
    return False


# EX 3
def great_42(a: int, b: int) -> bool:
    """
    Returns True if either a or b is 42, or if their sum or difference of a and
    b is 42. Otherwise return False.
    >>> great_42(-42, 0)
    True
    >>> great_42(5, 9)
    False
    >>> great_42(-40,-2)
    True
    >>> great_42(-37,4)
    False
    """
    if abs(a) == 42:
        return True
    elif abs(b) == 42:
        return True
    elif abs(a + b) == 42:
        return True
    elif abs(a - b) == 42:
        return True
    return False


# EX 4
def blackjack(a: int, b: int) -> int:
    """
    Returns the value closest to 21 but if both over 21 then its returns 0.
    >>> blackjack(7, 4)
    7
    >>> blackjack(666, 6)
    6
    >>> blackjack(666, 999)
    0
    >>> blackjack(3, 90)
    3
    """
    if a > 21 and b > 21:
        return 0
    elif a > 21 and b <= 21:
        return b
    elif b > 21 and a <= 21:
        return a
    elif a > b:
        return a
    elif b > a:
        return b
    

# EX 5
def sum_uniques(a: int, b: int, c: int) -> int:
    """
    Returns the sum of all three if all three digits are different. If any two
    digits are the same the program returns the value thats different and if 
    all three values are the same it returns 0.
    >>> sum_uniques(4, 4, 4)
    0
    >>> sum_uniques(4, 5, 6)
    15
    >>> sum_uniques(9, 9, 10)
    10
    """
    if a != b and b != c and c != a:
        return a + b + c
    elif a == b and b == c and a == c:
        return 0    
    elif a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b



#-----------------------------------------------------------------------------
# Main Script


# EX 1 answers
x = bakers_party(54, False)
print(x)
y = bakers_party(100, False)
print(y)
z = bakers_party(99, True)
print(z)


# EX 2 answers
x = squirrel_play(89, False)
print(x)
y = squirrel_play(91, False)
print(y)
z = squirrel_play(89, True)
print(z)


# EX 3 answers
x = great_42(-42, 0)
print(x)
y = great_42(5, 9)
print(y)
z = great_42(-40,-2)
print(z)
t = great_42(-37,4)
print(t)


# EX 4 answers
x = blackjack(7, 4)
print(x)
y = blackjack(666, 6)
print(y)
z = blackjack(666, 999)
print(z)
t = blackjack(3, 90)
print(t)


# EX 5 answers
x = sum_uniques(4, 4, 4)
print(x)
y = sum_uniques(4, 5, 6)
print(y)
z = sum_uniques(9, 9, 10)
print(z)