# Tauheed Alamgir 101194927

def big_diff(t: list) -> float:
    """
    Returns the difference between the largest and smallest number
    >>> big_diff([1,2,3,4,5,6,7,8,9,10])
    9
    >>> big_diff([32,67,51,38,94,56])
    62
    >>> big_diff([11,18,21,22,31,10,40])
    30
    """
    if (len(t) < 2):
        return 0 
    maxn = t[0]
    minn = t[0]
    for x in lst:
        if maxn < x:
            maxn = x
        elif minn > x:
            minn = x 
    return maxn - minn

lst = [1,2,3,4,5,6,7,8,9,10]
print(big_diff(lst))
lst = [32,67,51,38,94,56]
print(big_diff(lst))
lst = [11,18,21,22,31,10,40]
print(big_diff(lst))
