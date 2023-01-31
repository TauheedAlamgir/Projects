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
    s = km / 1.6093
    e = ( s - int(s) ) * 1760
    return(str(s) + " miles and " + str(e) + " yards" )

u = 5
print(convert(u))
p = 0
print(convert(p))
i = 1.6102144
print(convert(i))

def abc(a:bool, b:float) -> int:
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


def eculdist(a: float, b: float, c: float, d: float) -> float:
    """
    Returns the length of a line segment between two points
    >>> eculdist(2,3,4,5)
    2
    >>> eculdist(4.0,6.9,5.8,9.33)
    20.870900000000006
    >>> eculdist(4,5.7,2,999.9)
    995807.2999999999
    """
    x = a - b
    y = c - d
    return x ** 2 + y ** 2


p = eculdist(2,3,4,5)
print(p)
u = eculdist(4.0,6.9,5.8,9.33)
print(u)
i = eculdist(4,5.7,2,999.9)
print(i)



def mystery(lst: list) -> list:
    return [max(lst[0],lst[-l])] * 4










def area_of_circle(x1:'float',y1:'float' , x2:'float',y2:'float') -> 'float':
    """
       function that takes 2 points the cener of circle x1,y1
       and point on the permieter x2,y2 and returns the
       area of the circle
   """
   #calculate the distance between center and point
   #then find the area of that distance.
return area_of_disk(distance(x1,y1,x2,y2))

x1,y1 = 10,20
x2,y2 = 6,10

print("\nArea of Disk of radius 10 :",area_of_disk(10))

print("\nDistance between point ({},{}) , ({},{}) is {}".format(x1,y1,x2,y2,distance(x1,y1,x2,y2)))

print("\nArea of the circle for above points. ({},{}) , ({},{}) is {}".format(x1,y1,x2,y2,area_of_circle(x1,y1,x2,y2)))
