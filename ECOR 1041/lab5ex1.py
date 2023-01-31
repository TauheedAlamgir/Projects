# Tauheed Alamgir 101194927

def tip(t: float, a: float) -> float:
    """
    t is the amount paid by diners while a is the satisfactory level of diners
    Totally satisfied recieves a 20% tip
    Somewhat satisfied recieves a 15% tip
    Dissatisfied recieves a 5% tip
    >>> TP = tip(100, 2)
    15.0
    >>> TP = tip(89.6, 3)
    4.4799999999999995
    >>> TP = tip(32.87, 1) 
    6.574
    """
    if a == 1:
        return t * (20 / 100)
    elif a == 2:  
        return t * (15 / 100)
    elif a == 3:        
        return t * (5 / 100)   
    
TP = tip(100, 2)
print(TP)
TP = tip(89.6, 3)
print(TP)
TP = tip(32.87, 1)
print(TP)
