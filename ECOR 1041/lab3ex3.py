#Tauheed Alamgir 101194927

def accumulated_amount(principal, rate, n, time):
 return principal * ((1 + rate/n ) ** (n * time))

amount = accumulated_amount(1500, 0.043, 4, 6)
print(amount)
amount = accumulated_amount(0, 7.0, 5.0, 1)
print(amount)
amount = accumulated_amount(2, 0, 3.0, 9.0)
print(amount)
