# Tauheed Alamgir 101194927

# Ex 1
def factorial(n: int) -> int:
 """Return n! for positive values of n.
 >>> factorial(1)
 1
 >>> factorial(2)
 2
 >>> factorial(3)
 6
 >>> factorial(4)
 24
 """
 
 fact = 1
 for i in range(2,n+1):
  fact = fact * n
 return fact 


# Ex 2
def tip(m: float, p: float) -> float:
 """
 m is the amount paid while p is the satisfactory level
 satisfactory level 1 will be 20% tip
 satisfactory level 2 will be 15% tip
 satisfactory level 3 will be 5% tip
 m * (p / 100)
 >>> tips(125) 
 6.25
 >>> tips(32) 
 6.4
 >>> tips(57.78) 
 8.667
 """
 if p == 1 :
  return m * (20 / 100)
 elif p == 2 :
  return m * (15 / 100)
 else :
  return m * (5 / 100)
 
 
# Ex 3
def coupon(m: float) -> float:
 """
 m is float which could be less than 10 or between 10 and 60 or between
 60 and 150 or between 150 and 210 or more than 210 for which the coupon can
 be 0% or 8% or 10% or 12% or 14% respectively and multiply them which will 
 give you the amount of discount they shall recieve.
 >>> coupon(908)
 $127.12
 >>> coupon(5)
 $0.00
 >>> coupon(15)
 $1.20
 >>> coupon(100)
 $10.00
 >>> coupon(160)
 $19.20
 """
 
 if m < 10 :
  return m * (0 / 100)
 elif 10 <= m <= 60 :
  return m * (8 / 100)
 elif 60 <= m <= 150 :
  return m * (10 / 100)
 elif 150 <= m <= 210:
  return m * (12 / 100)
 else :
  return m * (14 / 100)


# Final Exercise
def test_int(response:str, expected:int, actual:int) -> int:
 """
 Returns
 >>> test_int(factorial, 1, 1)
 1 = test passed
 >>> test_int(factorial, 4, 24)
 0 = test failed
 >>> test_int(factorial, 2, 2)
 1 = test passed
 """
 
 print("expected result:", expected, "actual result:", actual)
 if actual == expected:
  test = 1
  print(test, "= test passed")
 else:
  test = 0
  print(test, "= test failed")
  return test
  


# Main Scirpt================================================================#



# Ex 1 answers
passed_tests = 0
failed_tests = 0
x = factorial(1)
print( "Testing factorial( 1 ) ")
print( "Expected result: 1, Actual result: ", x )
if x == 1 :
    print ("Test passed")
    passed_tests += 1
else:
    print ("Test failed")
    failed_tests += 1
 
y = factorial(2)
print( "Testing factorial( 2 ) ")
print( "Expected result: 2, Actual result: ", y )
if y == 2:
    print("Test passed")
    passed_tests += 1
else:
    print("Test failed")
    failed_tests += 1
    
z = factorial(3)
print( "Testing factorial( 3 ) ")
print( "Expected result: 6, Actual result: ", z )
if z == 6:
    print("Test passed")
    passed_tests += 1
else:
    print("Test failed")
    failed_tests += 1
    
s = factorial(4)
print( "Testing factorial( 4 ) ")
print( "Expected result: 24, Actual result: ", s )
if s == 24:
    print("Test passed")
    passed_tests += 1
else:
    print("Test failed")
    failed_tests += 1    
print(passed_tests,"tests passed for Exercise 1")
print(failed_tests,"tests failed for Exercise 1")


# Ex 2 answers
x = tip(125, 3)
print(x)
y = tip(32, 1)
print(y)
z = tip(57.78, 2)
print(z)


# Ex 3 answers
x = coupon(908)
print("${:,.2f}".format(x))
y = coupon(5)
print("${:,.2f}".format(y))
z = coupon(15)
print("${:,.2f}".format(z))
v = coupon(100)
print("${:,.2f}".format(v))
u = coupon(160)
print("${:,.2f}".format(u))


# Final Exercise answers
x = test_int(factorial, 1, 1)
y = test_int(factorial, 4, 24)
z = test_int(factorial, 2, 2)
