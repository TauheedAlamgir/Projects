#Tauheed Alamgir 101194927

import math

#Ex 1
def area_of_disk(radius):
 return math.pi * radius ** 2

def area_of_ring(outer, inner):
 return area_of_disk(outer) - area_of_disk(inner)

#Ex 2
LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
 return 100 * LITRES_PER_GALLON / KMS_PER_MILE / mpg

#Ex 3
def accumulated_amount(principal, rate, n, time):
 return principal * ((1 + rate/n ) ** (n * time))

#Ex 4
import math
def area_of_cone(height, radius):
 return math.pi * radius * (math.sqrt(radius ** 2) + (height ** 2))

#Ex 1 answers
area = area_of_disk(5)
print(area)
area = area_of_disk(5.0)
print(area)
area = area_of_ring(10, 5)
print(area)
area = area_of_ring(10.0, 5.0)
print(area)

#Ex 2 answers 
print(convert_to_litres_per_100_km(32))
#print(convert_to_litres_per_100_km(0))
#It works with integer numbers but not with real numbers

#Ex 3 answers
amount = accumulated_amount(1500, 0.043, 4, 6)
print(amount)
amount = accumulated_amount(0, 1, 3, 5)
print(amount)
amount = accumulated_amount(7, 0, 4, 1)
print(amount)

#Ex 4 answers
area = area_of_cone(6, 12)
print(area)
#When using these two values we get a float
area = area_of_cone(0, 9)
print(area)
#Also when use these values you will also get a float
area = area_of_cone(8, 0)
print(area)
#When we put the radius as 0 it gives 0.0 which is float




def centered_average(list):   
   return (sum(list) - max(list) - min(list)) / (len(list) - 2)
   
num = [1,1,5,5,10,8,7]

print ("centered average of the list :", centered_average(num))


def j(lst: list) -> float:
 sum = 0
 skip = 0
 
 


def equality(x: int) -> int:

 """

 Returns the value we are assigning to it x=x

 >>> equality(9)

 9

 >>> equality(0)

 0

 """

 if (x!=0):

  return -x

 else:

  return x

y = equality(9)

print(9)

u = equality(0)

print(0)


def evens(lst: list) -> list:
    t = []
    for ele in lst:
        if ele % 2 == 0:
        
