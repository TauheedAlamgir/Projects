# Tauheed Alamgir  101194927


# Automated Testing function
def test(function, expected, n):
    actual = function(n)
    if actual == expected:
        return 1
    else: return 0

def test(des, expected, actual):
    print(des)
    print("expected result:", expected, "actual result:", actual)
    if expected == actual:
        print("Test Passed")
        return 1
    else:
        print("Test Failed")
        return 0

# Exercise 1
def count_evens(lst: list) -> int:
    """
    Returns how many even digits we have in our list
    >>> count_evens([9,8,7,6,5,4])
    3
    >>> count_evens([12,345,76,54,98,87,90])
    5
    >>> count_evens([])
    0
    >>> count_evens([-3,-9,9,-6,4])
    2
    """
    t = 0
    for ele in lst:
        if ele % 2 == 0:
            t += 1
    return t

       
# Exercise 2
def big_diff(lst: list) -> int:
    """
    Returns the diffrence between the largest and smallest number in the list
    >>> big_diff([9,9,8,7,6,5])
    4
    >>> big_diff([908,685,986,424,575,734])
    562
    >>> big_diff([88,77,90,56,34,66])
    56
    """
    smallest = lst [0]
    for num in lst:
        smallest = min (smallest, num)
        largest = lst [0]
    for num in lst:
        largest = max (largest, num)
    return largest - smallest


# Exercise 3
def has22(lst: list) -> bool :
    """
    Returns True if the list has a 2 beside a 2 or else returns False
    >>> has22([3,6,2,2,9])
    True
    >>> has22([1,2,3,4,5,6,7])
    False
    >>> has22([5,8,6,2,2,9,4])
    True
    """
    t = 0
    for t in range(len(lst)):
        if lst [t] == 2 and lst [t - 1] == 2 :
            return True
    return False


# Exercise 4
def centered_average(lst: list) -> float :
    """
    Returns the average of the list excluding the largest and smallest and if 
    theres multiple same large or small number the code ignores one of them
    >>> centered_average([9,8,7,6])
    7.5
    >>> centered_average([5,5,4,3,2,1])
    3.5
    >>> centered_average([9,6,8,8,2,0,6])
    6.0
    """
    smallest = lst [0]
    for a in lst:
        smallest = min (smallest, a)
    largest = lst [0]
    for a in lst:    
        largest = max (largest, a)
    sum = 0               
    for a in lst:    
        sum += a    
    return (sum - smallest - largest) / (len(lst) - 2)


# Exercise 5
def sum13(lst: list) -> float:
    """
    Returns the sum of the list excluding any 13 or any digit after 13 and if 
    list is empty it returns 0
    >>> sum13([13,4,5,6,7])
    18
    >>> sum13([16,13,78,5,9])
    30
    >>> sum13([])
    0
    """
    sum = 0
    skip = 0
    while skip < len (lst):
        if lst [skip] == 13:
            skip += 1
        else:
            sum += lst [skip]
        skip += 1
    return sum


# Exercise 6
def sum67(lst: list) -> float:
    """
    Returns the sum of the list excluding 6 and 7 or any digits in between
    6 and 7 in the list
    >>> sum67([1,2,3,4,5,6,7,8,9])
    32
    >>> sum67([6,8,4,5,3,2,1,7])
    0
    >>> sum67([34,56,6,666666666,9,7])
    90
    """
    add = True                              # Means we could add the digits
    sum = 0
    for n in lst:
        if n == 6:                          # Once its 6 we change it to false
            add = False
        elif add:
            sum += n                        # Adds the value if it was not 6
        elif not add and n == 7:            # not add = False
            add = True
    return sum


# Exercise 7
def bank_statement(lst: list) -> list:
    """
    Returns the deposit amount, withdrawal amount and the current amount
    balance to two digits of precision after the decimal point
    >>> bank_statement([9.7, -9, 8, 5.67])
    [23.37, -9, 14.37]
    >>> bank_statement([888, -555, 666,999])
    [2553, -555, 1998]
    >>> bank_statement([7765, -987, 6])    
    [7771, -987, 6784]
    """
    Deposit = 0
    Withdrawal = 0
    for n in range(len(lst)):
        if lst [n] > 0:
            Deposit += lst [n]
        if lst [n] < 0:
            Withdrawal += lst [n]
    return [round(Deposit, 2), round(Withdrawal, 2), round(Deposit + Withdrawal, 2)] 

             
# Exercise 8
def divisors(n: int) -> list: 
    """
    Returns the divisors of the digit we have entered
    >>> divisors(100)
    [1 2 4 5 10 20 25 50 100]
    >>> divisors(8)
    [1 2 4 8]
    >>> divisors(66)
    [1 2 3 6 11 22 33 66]
    """
    lst1 = []
    for t in range(1, n):
        if n % t == 0:
            lst1 += [t]
    return lst1 + [n]


# Exercise 9
def reverse(lst: list) -> list:
    """
    Return the reverse of the list we have entered
    >>> reverse([1,2,3,4,5,6,7,8,9])
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> reverse([666,888,777,555,999,111,333])
    [333, 111, 999, 555, 777, 888, 666]
    >>> reverse([25437,678954,26715,905836,21754])
    [21754, 905836, 26715, 678954, 25437]
    """
    total = [0] * len(lst)
    for n in range(len(lst)):
        total [len(lst) - n - 1] = lst[n]
    return total

    
    

# -------------------------------------------------------------------------- #
# Main Scirpt



# Exercise 1
passed_tests1 = 0
failed_tests1 = 0
lst = [9,8,7,6,5,4]
actual = count_evens(lst)
x = test(lst,3,actual)
if x == 1 :
    passed_tests1 += 1
else:
    failed_tests1 += 1
lst = [12,345,76,54,98,87,90]
actual = count_evens(lst)
x = test(lst,5,actual)
if x == 1 :
    passed_tests1 += 1
else:
    failed_tests1 += 1
lst = []
actual = count_evens(lst)
x = test(lst,0,actual)
if x == 1 :
    passed_tests1 += 1
else:
    failed_tests1 += 1
lst = [-3,-9,9,-6,4]
actual = count_evens(lst)
x = test(lst,2,actual)
if x == 1 :
    passed_tests1 += 1
else:
    failed_tests1 += 1
print(passed_tests1,"tests passed for Exercise 1")
print(failed_tests1,"tests failed for Exercise 1")


# Exercise 2
passed_tests2 = 0
failed_tests2 = 0
lst = [9,9,8,7,6,5]
actual = big_diff(lst)
x = test(lst,4,actual)
if x == 1 :
    passed_tests2 += 1
else:
    failed_tests2 += 1
lst = [908,685,986,424,575,734]
actual = big_diff(lst)
x = test(lst,562,actual)
if x == 1 :
    passed_tests2 += 1
else:
    failed_tests2 += 1
lst = [88,77,90,56,34,66]
actual = big_diff(lst)
x = test(lst,56,actual)
if x == 1 :
    passed_tests2 += 1
else:
    failed_tests2 += 1
print(passed_tests2,"tests passed for Exercise 2")
print(failed_tests2,"tests failed for Exercise 2")


# Exercise 3
passed_tests3 = 0
failed_tests3 = 0
lst = [3,6,2,2,9]
actual = has22(lst)
x = test(lst,True,actual)
if x == 1 :
    passed_tests3 += 1
else:
    failed_tests3 += 1
lst = [1,2,3,4,5,6,7]
actual = has22(lst)
x = test(lst,False,actual)
if x == 1 :
    passed_tests3 += 1
else:
    failed_tests3 += 1
lst = [5,8,6,2,2,9,4]
actual = has22(lst)
x = test(lst,True,actual)
if x == 1 :
    passed_tests3 += 1
else:
    failed_tests3 += 1
print(passed_tests3,"tests passed for Exercise 3")
print(failed_tests3,"tests failed for Exercise 3")


# Exercise 4
passed_tests4 = 0
failed_tests4 = 0
lst = [9,8,7,6]
actual = centered_average(lst)
x = test(lst,7.5,actual)
if x == 1 :
    passed_tests4 += 1
else:
    failed_tests4 += 1
lst = [5,5,4,3,2,1]
actual = centered_average(lst)
x = test(lst,3.5,actual)
if x == 1 :
    passed_tests4 += 1
else:
    failed_tests4 += 1
lst = [9,6,8,8,2,0,6]
actual = centered_average(lst)
x = test(lst,6.0,actual)
if x == 1 :
    passed_tests4 += 1
else:
    failed_tests4 += 1
print(passed_tests4,"tests passed for Exercise 4")
print(failed_tests4,"tests failed for Exercise 4")


# Exercise 5
passed_tests5 = 0
failed_tests5 = 0
lst = [13,4,5,6,7]
actual = sum13(lst)
x = test(lst,18,actual)
if x == 1 :
    passed_tests5 += 1
else:
    failed_tests5 += 1
lst = [16,13,78,5,9]
actual = sum13(lst)
x = test(lst,30,actual)
if x == 1 :
    passed_tests5 += 1
else:
    failed_tests5 += 1
lst = []
actual = sum13(lst)
x = test(lst,0,actual)
if x == 1 :
    passed_tests5 += 1
else:
    failed_tests5 += 1
print(passed_tests5,"tests passed for Exercise 5")
print(failed_tests5,"tests failed for Exercise 5")


# Exercise 6
passed_tests6 = 0
failed_tests6 = 0
lst = [1,2,3,4,5,6,7,8,9]
actual = sum67(lst)
x = test(lst,32,actual)
if x == 1 :
    passed_tests6 += 1
else:
    failed_tests6 += 1
lst = [6,8,4,5,3,2,1,7]
actual = sum67(lst)
x = test(lst,0,actual)
if x == 1 :
    passed_tests6 += 1
else:
    failed_tests += 1
lst = [34,56,6,666666666,9,7]
actual = sum67(lst)
x = test(lst,90,actual)
if x == 1 :
    passed_tests6 += 1
else:
    failed_tests6 += 1
print(passed_tests6,"tests passed for Exercise 6")
print(failed_tests6,"tests failed for Exercise 6")


# Exercise 7
passed_tests7 = 0
failed_tests7 = 0
lst = [9.7, -9, 8, 5.67]
actual = bank_statement(lst)
x = test(lst,[23.37, -9, 14.37],actual)
if x == 1 :
    passed_tests7 += 1
else:
    failed_tests7 += 1
lst = [888, -555, 666,999]
actual = bank_statement(lst)
x = test(lst,[2553, -555, 1998],actual)
if x == 1 :
    passed_tests7 += 1
else:
    failed_tests7 += 1
lst = [7765, -987, 6]    
actual = bank_statement(lst)
x = test(lst,[7771, -987, 6784],actual)
if x == 1 :
    passed_tests7 += 1
else:
    failed_tests7 += 1
print(passed_tests7,"tests passed for Exercise 7")
print(failed_tests7,"tests failed for Exercise 7")


# Exercise 8
passed_tests8 = 0
failed_tests8 = 0
lst = 100
actual = divisors(lst)
x = test(lst,[1, 2, 4, 5, 10, 20, 25, 50, 100],actual)
if x == 1 :
    passed_tests8 += 1
else:
    failed_tests8 += 1
lst = 8
actual = divisors(lst)
x = test(lst,[1, 2, 4, 8],actual)
if x == 1 :
    passed_tests8 += 1
else:
    failed_tests8 += 1
lst = 66
actual = divisors(lst)
x = test(lst,[1, 2, 3, 6, 11, 22, 33, 66],actual)
if x == 1 :
    passed_tests8 += 1
else:
    failed_tests8 += 1
lst = 100
actual = divisors(lst)
x = test(lst,[1, 2, 4, 5, 10, 20, 25, 50, 100],actual)
if x == 1 :
    passed_tests8 += 1
else:
    failed_tests8 += 1
print(passed_tests8,"tests passed for Exercise 8")
print(failed_tests8,"tests failed for Exercise 8")


# Exercise 9
passed_tests9 = 0
failed_tests9 = 0
lst = [1,2,3,4,5,6,7,8,9]
actual = reverse(lst)
x = test(lst,[9, 8, 7, 6, 5, 4, 3, 2, 1],actual)
if x == 1 :
    passed_tests9 += 1
else:
    failed_tests9 += 1
lst = [666,888,777,555,999,111,333]
actual = reverse(lst)
x = test(lst,[333, 111, 999, 555, 777, 888, 666],actual)
if x == 1 :
    passed_tests9 += 1
else:
    failed_tests9 += 1
lst = [25437,678954,26715,905836,21754]
actual = reverse(lst)
x = test(lst,[21754, 905836, 26715, 678954, 25437],actual)
if x == 1 :
    passed_tests9 += 1
else:
    failed_tests9 += 1
print(passed_tests9,"tests passed for Exercise 9")
print(failed_tests9,"tests failed for Exercise 9")



def max(lst):
    maxi = lst[0] 
    mini = lst[0]
    for m in lst:
        if maxi < m:
            maxi = m
    for m in lst:
        if mini > m:
            mini = m
    return maxi - mini
b = [1,7,9,12,5]
print (max(b))


