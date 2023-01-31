# Tauheed Alamgir 101194927

def squirrel_play(a: int, b: bool) -> bool:
    """
    Returns false if squirrels can play outside when temperature is between 60 
    and 90 unless summer and its between 60 and 100 then it returns True
    >>> sq = squirrel_play(69, False)
    True
    >>> sq = squirrel_play(87, True)
    True
    >>> sq = squirrel_play(34, False)
    False
    """
    if (a >= 60) and (a <= 90):
        return True
    elif (a >= 60) and (a <= 100) and b:
        return True
    return False

sq = squirrel_play(69, False)
print(sq)
sq = squirrel_play(87, True)
print(sq)
sq = squirrel_play(34, False)
print(sq)
