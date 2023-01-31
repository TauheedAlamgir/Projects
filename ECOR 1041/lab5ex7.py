# Tauheed Alamgir 101194927

def blackjack(x: int, y: int) -> int:
    """
    Returns value closest to 21 between x and y but if both digits are over 21 
    then it will return 0.
    >>> BJ = blackjack(5, 3)
    5
    >>> BJ = blackjack(643, 23)
    0
    >>> BJ = blackjack(54, 2)
    2
    >>> BJ = blackjack(19, 78)
    19
    """
    if (x > 21) and (y > 21):
        return 0
    elif (x > 21) and (y <= 21):
        return y
    elif (y > 21) and (x <= 21):
        return x
    elif x > y:
        return x
    elif y > x:
        return y
    
BJ = blackjack(5, 3)
print(BJ)
BJ = blackjack(643, 23)
print(BJ)
BJ = blackjack(54, 2)
print(BJ)
BJ = blackjack(19, 78)
print(BJ)
