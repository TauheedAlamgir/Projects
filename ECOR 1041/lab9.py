# Tauheed Alamgir 101194927

# Exercise 1
def first_last6(lst: list) -> bool :
    """
    Returns True if the first or last or both digits of the list is 6, if not 
    returns False
    >>> first_last6([2, 3, 4, 5, 6, 7, 8, 6])
    True
    >>> first_last6([6, 7, 8 , 9, 4, 7])
    True
    >>> first_last6([8, 8, 8, 8, 8, 8, 8])
    False
    >>> first_last6([6, 4, 3, 2, 1, 6])
    True
    >>> first_last6([7, 6, 6, 6, 6, 6, 8])
    False
    """
    if lst[0] == 6 or lst[-1] == 6:
        return True
    return False


# Exercise 2
def same_first_last(lst: list) -> bool :
    """
    Returns True if its not an empty list and first and the last digit are the
    same, if not then returns False
    >>> same_first_last([9, 0, 9, 0, 9]
    True
    >>> same_first_last([])
    False
    >>> same_first_last([9, 8, 7, 6, 5, 4, 3, 2, 1])
    False
    """
    if len(lst) == 0:
        return False
    if lst[0] == lst[-1]:
        return True
    return False


# Exercise 3
def make_pi() :
    """
    Return the first three digits from pi 
    >>> make_pi()
    [3, 1, 4]
    """
    return [3, 1, 4]


# Exercise 4
def common_end(a: list, b: list) -> bool :
    """
    Returns a True if they have the same first element or the same 
    last element or if both the first and last elements of both lists are the
    same if none of that happens then it returns False
    >>> common_end([1, 2, 4, 3], [7, 3, 4, 3])
    True
    >>> common_end([1, 1, 1, 1], [1, 2, 3, 4])
    True
    >>> common_end([2, 3, 4, 2], [3, 4, 5, 3])
    True
    >>> common_end([2,3,4,5], [3,4,5,7])
    False
    """
    if (a[0] == b[0]) or (a[-1] == b[-1]):
        return True
    elif (a[0] == a[-1]) and (b[0] == b[-1]):
        return True
    return False


# Exercise 5
def sum3(sums: list) -> int :
    """
    Returns the sum of the 3 digits
    >>> sum3([9, 8, 9])
    26
    >>> sum3([898, 69, 666])
    1633
    >>> sum3([1, 1000, 3])
    1004
    """
    return sums [0] + sums [1] + sums [2]


# Exercise 6
def rotate_left3(rotlef: list) -> str:
    """
    Returns a left shift to each digit in the list creating a new list
    >>> rotate_left3([1, 2, 3])
    [2, 3, 1]
    >>> rotate_left3([666, 999, 888])
    [999, 888, 666]
    >>> rotate_left3([7, 5, 6])
    [5, 6, 7]
    """
    return [rotlef [1], rotlef [2], rotlef [0]]


# Exercise 7
def reverse3(rev: list) -> str:
    """
    Returns the reverse of list as a new list
    >>> reverse3([1, 2, 3])
    [3, 2, 1]
    >>> reverse3([666, 777, 888])
    [888, 777, 666]
    >>> reverse3([6, 7, 8])
    [8, 7, 6]
    """
    return [rev [2], rev [1], rev [0]]


# Exercise 8
def max_end3(big: list) -> str:
    """
    Returns the larger first or last digit as a new list as big as the original
    >>> max_end3([1, 5, 3])
    [3, 3, 3]
    >>> ymax_end3([666, 8, 9])
    [666, 666, 666]
    >>> max_end3([9, 8, 7])
    [9, 9, 9]
    """
    if big [0] > big [2]:
        return [big [0], big [0], big [0]]
    else:
        return [big [2], big [2], big [2]]
    

# Exercise 9
def sum2(digit: list) -> str:
    """
    Returns the sum of the list, if no digits returns 0, if one digit returns 
    the digit itself
    >>> sum2([666,3])
    669
    >>> sum2([])
    0
    >>> sum2([5])
    5
    """
    if len(digit) == 0:
        return 0
    elif len(digit) == 1:
        return digit [0]
    else:
        return digit [0] + digit [1]


# Exercise 10
def middle_way(a: list, b:list) -> str:
    """
    Returns the middle digit of both lists as a new list
    >>> middle_way([9, 6, 3], [2, 4, 6])
    [6, 4]
    >>> middle_way([555, 696, 777], [999, 969, 888])
    [696, 969]
    >>> middle_way([90, 89, 78], [12, 23, 34])
    [89, 23]
    """
    return [a [1], b [1]]


# Exercise 11
def make_ends(ends: list) -> str:
    """
    Returns the first and the last digit as a new list
    >>> make_ends([9, 8, 7, 666])
    [9, 666]
    >>> make_ends([1, 2, 3, 4])
    [1, 4]
    >>> make_ends([8888, 7777, 4332, 56789, 34567])
    [8888, 34567]
    """
    return [ends [0], ends[len(ends) - 1]]


# Exercise 12
def has23(lst: list) -> bool:
    """
    Returns True or False if the list has 2 or 3 in it
    >>> has23([2, 6, 8, 9])
    True
    >>> has23([2, 3, 4, 5])
    True
    >>> has23([6, 3, 7, 9])
    True
    >>> has23([8, 9, 7, 666])
    False
    """
    if 2 in lst or 3 in lst:
        return True
    else:
        return False
    


# ------------------------------------------------------------------------- #
# Main Script



# Exercise 1
x = [2, 3, 4, 5, 6, 7, 8, 6]
print(first_last6(x))
y = [6, 7, 8 , 9, 4, 7]
print(first_last6(y))
z = [8, 8, 8, 8, 8, 8, 8]
print(first_last6(z))
w = [6, 4, 3, 2, 1, 6]
print(first_last6(w))
t = [7, 6, 6, 6, 6, 6, 8]
print(first_last6(t))


# Exercise 2
x = [9, 0, 9, 0, 9]
print(same_first_last(x))
y = []
print(same_first_last(y))
z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(same_first_last(z))


# Exercise 3
print(make_pi())


# Exercise 4
x = [1, 2, 4, 3]
y = [7, 3, 4, 3]
print(common_end(x, y))
p = [1, 1, 1, 1]
o = [1, 2, 3, 4]
print(common_end(p, o))
k = [2, 3, 4, 2]
l = [3, 4, 5, 3]
print(common_end(k, l))
j = [2,3,4,5]
m = [3,4,5,7]
print(common_end(j, m))


# Exercise 5
x = [9, 8, 9]
print(sum3(x))
y = [898, 69, 666]
print(sum3(y))
z = [1, 1000, 3]
print(sum3(z))


# Exercise 6
x = [1, 2, 3]
print(rotate_left3(x))
y = [666, 999, 888]
print(rotate_left3(y))
z = [7, 5, 6]
print(rotate_left3(z))


# Exercise 7
x = [1, 2, 3]
print(reverse3(x))
y = [666, 777, 888]
print(reverse3(y))
z = [6, 7, 8]
print(reverse3(z))


# Exercise 8
x = [1, 5, 3]
print(max_end3(x))
y = [666, 8, 9]
print(max_end3(y))
z = [9, 8, 7]
print(max_end3(z))


# Exercise 9
x = [666,3]
print(sum2(x))
y = []
print(sum2(y))
z = [5]
print(sum2(z))


# Exercise 10
x = [9, 6, 3]
y = [2, 4, 6]
print(middle_way(x, y))
p = [555, 696, 777]
o = [999, 969, 888]
print(middle_way(p, o))
k = [90, 89, 78]
l = [12, 23, 34]
print(middle_way(k, l))


# Exercise 11
x = [9, 8, 7, 666]
print(make_ends(x))
y = [1, 2, 3, 4]
print(make_ends(y))
z = [8888, 7777, 4332, 56789, 34567]
print(make_ends(z))


# Exercise 12
x = [2, 6, 8, 9]
print(has23(x))
y = [2, 3, 4, 5]
print(has23(y))
z = [6, 3, 7, 9]
print(has23(z))
t = [8, 9, 7, 666]
print(has23(t))
