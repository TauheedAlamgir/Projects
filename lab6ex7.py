# Tauheed Alamgir 101194927

def centered_average(t: list) -> float:
    """
    Returns the average of list excluding the largest and smallest number and if
    one number is repeated it counts it as one
    >>> centered_average([1,2,3,4,5,6,7,8,9])
    5.0
    >>> centered_average([1,2,2,3,4,5,99])
    3.2
    >>> centered_average([8,5,6,2,5,1,3])
    4.2
    """
    small = t[0]
    for x in t:
        small = min(small, x)
    large = t[0]
    for x in t:    
        large = max(large, x)
    sum = 0               
    for x in t:    
        sum = sum + x #sum += x  
    return (sum - small - large) / (len(t) - 2)

a = [1,2,3,4,5,6,7,8,9]
print(centered_average(a))
a = [1,2,2,3,4,5,99]
print(centered_average(a))
a = [8,5,6,2,5,1,3]
print(centered_average(a))