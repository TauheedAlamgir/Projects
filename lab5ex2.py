# Tauheed Alamgir 101194927

def coupon(t: float) -> float:
    """
    t is float which will be in between numbers according to which they will 
    get discounts
    >>> cou = coupon(789)
    110.46000000000001
    >>> cou = coupon(159)
    19.08
    >>> cou = coupon(211)
    29.540000000000003
    >>> cou = coupon(19)
    1.52
    >>> cou = coupon(1)
    0.0
    """
    if t < 10:
        return t * (0 / 100)
    elif 10 <= t <= 60:
        return t * (8 / 100)
    elif 60 < t <= 150:  
        return t * (10 / 100) 
    elif 150 < t <= 210:  
        return t * (12 / 100) 
    elif t > 210:
        return t * (14 / 100)
    
cou = coupon(789)
print(cou)
cou = coupon(159)
print(cou)
cou = coupon(211)
print(cou)
cou = coupon(19)
print(cou)
cou = coupon(1)
print(cou)