# Tauheed Alamgir 101194927


# Exercise 1
#>>> point1 = [1.0, 2.0]
#>>> point1
# Step 1
# What is displayed when Python evaluates point1?
# [1.0, 2.0]


# Step 2
#>>> point1.append(3.0)
#>>> point1
# What is displayed when Python evaluates point1?
# [1.0, 2.0, 3.0]
#>>> point1.pop(0) # Remove the item at index 0 in the list
#>>> point1
#>>> point1.pop() # Remove the last item in the list
#>>> point1
# What is displayed when Python evaluates point1?
# [2.0, 3.0]
# In the second step point1.pop() the function removes 3.0 from our list 
# [2.0]


# Step 3
#>>> point1 = (1.0, 2.0)
#>>> type(point1)
#>>> point1
# What is displayed when the last two statements are evaluated?
# first statement shows <class 'tuple'>
# second statement shows (1.0, 2.0)


# Step 4
#>>> x = point1[0]
#>>> y = point1[1]
#>>> x
#>>> y
# What is displayed when Python evaluates x and y?
# x
# 1.0
# y
# 2.0
#>>> point2 = (4.0, 6.0)
#>>> x, y = point2
#>>> x
#>>> y
# What is displayed when Python evaluates x and y?
# x
# 4.0
# y
# 6.0


# Step 5
#>>> point2[0] = 2.0 # Can we change the point to (2.0, 6.0)? No
#  What is displayed when Python executes each statement? 
# First statement shows
# Traceback (most recent call last):
#  Python Shell, prompt 21, line 1
# builtins.TypeError: 'tuple' object does not support item assignment
#>>> point2.append(4.0) # Can we add a third coordinate? No
# Second statement shows
# Traceback (most recent call last):
#  Python Shell, prompt 22, line 1
# builtins.AttributeError: 'tuple' object has no attribute 'append'
#>>> point2.pop(0) # Can we remove the first coordinate? No
# Third statement shows
# Traceback (most recent call last):
#  Python Shell, prompt 23, line 1
# builtins.AttributeError: 'tuple' object has no attribute 'pop'


# Step 6
# It shows us that we can have lists that contain lists and tuples that 
# contain tuples
# >>> points = [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)]
# >>> points[0]
# >>> points[1]
# >>> points[2]
# points[0]
# (1.0, 5.0)
# points[1]
# (2.0, 8.0)
# points[2]
# (3.5, 12.5)


# Exercise 2
def average(tuples):
    """
    Returns a new tuple list at the same position in the original list
    as it takes only non negative numbers
    >>> x = [(1,9,6),(9,8,7),(333,666,999)]
    [(5, 5, 5), (8, 8, 8), (666, 666, 666)]
    >>> y = [(1,97,61),(45,88,67),(696,969,696)]
    [(53, 53, 53), (66, 66, 66), (787, 787, 787)]
    >>> z = [(34,867,1782),(345,2547,1735),(1893,6734,379)]
    [(894, 894, 894), (1542, 1542, 1542), (3002, 3002, 3002)]
    """
    result = []
    for a in tuples:
        average = ( sum(a) // 3)
        result.append((average, average, average))
    return result

# Exercise 2 answers
x = [(1,9,6),(9,8,7),(333,666,999)]
print(average(x))
y = [(1,97,61),(45,88,67),(696,969,696)]
print(average(y))
z = [(34,867,1782),(345,2547,1735),(1893,6734,379)]
print(average(z))


# Exercise 3
# Step 1
#>>> points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}
#>>> points
# What is displayed when points is evaluated?
# {(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}

#>>> point1 = (1.0, 2.0)
#>>> point2 = (4.0, 6.0)
#>>> point3 = (10.0, -2.0)
#>>> points = {point1, point2, point3}
#>>> points
# What is displayed when points is evaluated? 
# {(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}

#>>> points = set()
#>>> points.add(point1)
#>>> points.add(point2)
#>>> points.add(point3)
#>>> points
# What is displayed when points is evaluated?
# {(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}


# Step 2
#>>> points.add(point2)
#>>> points
# How many copies of point (4.0, 6.0) are in the set?
# It still prints 1 copy of (4.0, 6.0)


# Step 3
#>>> points[0]
#  What is displayed when points[0] is evaluated?
# Traceback (most recent call last):
#   Python Shell, prompt 16, line 1
# builtins.TypeError: 'set' object is not subscriptable


# Step 4
#>>> for point in points:
#... print(point)
#...
# What is displayed when this loop is executed?
# (1.0, 2.0)
# (10.0, -2.0)
# (4.0, 6.0)


# Exercise 4
def sum_x(a: list) -> float:
    """
    Returns the sum of all the x coordinates we have entered
    >>> x = ({(9.9, 7.6), (67.5, 57.4)})
    77.4
    >>> y = ({(666, 777), (234.7, 9864.7)})
    900.7
    >>> z = ({(66.6, 243.6), (32.78, 78.433), (7.12, 55, 999)})  
    106.5
    """
    sum = 0
    for item in a:
        sum += item[0]
    return sum



# -------------------------------------------------------------------------- #
# Main Scirpt



# Exercise 2 answers
x = [(1,9,6),(9,8,7),(333,666,999)]
print(average(x))
y = [(1,97,61),(45,88,67),(696,969,696)]
print(average(y))
z = [(34,867,1782),(345,2547,1735),(1893,6734,379)]
print(average(z))


# Exercise 4 answers
x = ({(9.9, 7.6), (67.5, 57.4)})
print(sum_x(x))
y = ({(666, 777), (234.7, 9864.7)})
print(sum_x(y))
z = ({(66.6, 243.6), (32.78, 78.433), (7.12, 55, 999)})  
print(sum_x(z))



def evens(lst: list) -> list:
    """
    """
    t = []                     # REVERSE FUNCTION
    for ele in lst:
        if ele % 2 == 0:
            t += [ele]
    for i in range (0,len(t)):
        for j in range (i + 1, len (t)): 
            if (t[i]<t[j]):
                t[i],t[j]= t[j],t[i]    
    return t

x = [66,2,5,77,3,4,98]
print(evens(x))

def generation(m: int) -> str:
    """
    """
    if m < 1946 :
        return "Boomer"
    elif 1946 <= m <= 1964 :
        return "boo"
    elif 1965 <= m <= 1980 :
        return "uuu"
    elif 1981 <= m <= 1996:
        return "iii"
    elif 1997 <= m <= 2015:
        return "ooo"
    else:
        return "Kiddo"
    
a = 1978
print(generation(a))
 
 
 
 
 
def convert(km: float) -> str:
    """
    Returns a string containing the length in miles and yards
    that is equivalent to km kilometers.
    Note that there are 1760 yards in a mile, and 1 mile is 1.6093 km.
    Assume that km is non-negative (error checking is not required).
    >>> convert(5)
    '3 miles and 188.22 yards' 
            # it is fine if it returns something like:
            # '3.0 miles and 188.21599..... yards' for all examples
    >>> convert(0)
    '0 miles and 0.0 yards'
    >>> convert(1.6102144)
    '1 miles and 1.0 yards' # don't worry about singular/plural 
    """
    a = km / 1.6093
    y = a * 1760
    return(str(x) + " miles and " + str(y) + " yards" )

u = 783
print(convert(u))
p = 345
print(convert(p))
i = 5.0
print(convert(i))

def abc(a:bool, b:float)->int :
    """
    function has a or b then it will return int.

    """
    if a == b:
        return b 
    if b == a:
        return a   
    else:
        return int(a + b)
    
x = True
y = 7.0
print(abc(x,y))
u = False
i = 9.8
print(abc(u,i))
p = True
o = 0.5
print(abc(p,o))
