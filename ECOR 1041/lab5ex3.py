# Tauheed Alamgir 101194927

def assistance(a: float, c: int) -> float:
    """
    Returns the assistance required by a family accoring to their income
    >>> assis = assistance(21090,3)
    3000
    >>> assis = assistance(17612,1)
    2000
    >>> assis = assistance(36023,6)
    9000
    """
    if (30000 <= a < 40000) and (c >= 3):
        return 1500 * c
    if (20000 <= a < 30000) and (c >= 2):
        return 1000 * c
    elif a < 20000:
        return 2000 * c
    
    
assis = assistance(21090,3)
print(assis)
assis = assistance(17612,1)
print(assis)
assis = assistance(36023,6)
print(assis)
