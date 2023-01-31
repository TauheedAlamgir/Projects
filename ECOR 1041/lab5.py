# Tauheed Alamgir 101194927

# Ex 1
def min_RRIF_withdrawal(RRIF: float, age: int) -> float:
    #RRIF is the withdrawal amount.
    """
    Return the value of RRIF where RRIF is divided by X where X = 90 - age
    which was given to us in the question and RRIF is a float and age is an int.
    >>> min_RRIF_withdrawal(6900.0, 55)
    197.1428571
    >>> min_RRIF_withdrawal(8800.0, 70)
    440
    >>> min_RRIF_withdrawal(90000.87, 65)
    3600.0348
    """
    X = 90 - age
    return RRIF / X

# Ex 2
def accrued_amount(P: float, r: float, t: int, n: int) -> float:
    # Principal is the same as P, rate is the same as r, time is the same as t. 
    """
    Return the A = P(1 + r/n)^tn which helps us calculate the accrued amount
    it does it by dividing r by a 100 then dividing it by n and adding 1 to it 
    the raising it to the power t multiplied by n then multiply the whole thing
    by the principal.
    >>> accrued_amount(700.9, 0.7, 1, 7)
    701.24
    >>> accrued_amount(650, 0.3, 1, 3)
    650.06
    >>> accrued_amount(440, 0.1, 1, 5)
    440.02
    """
    return P * ((1 + (r / 100) / n) ** (n * t)) # This calulates accrued amount

# Main scirpt Ex 1
a = min_RRIF_withdrawal(6900.0, 55)
print(a)
b = min_RRIF_withdrawal(8800.0, 70)
print(b)
c = min_RRIF_withdrawal(90000.87, 65)
print(c)
help(min_RRIF_withdrawal)

# Main script Ex 2
a = accrued_amount(700.9, 0.007, 1, 7)
print(a)
b = accrued_amount(650, 0.3, 1, 3)
print(b)
c = accrued_amount(440, 0.4, 1, 6)
print(c)
help(accrued_amount)
    
    
    


 



 
