#Tauheed Alamgir 101194927

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
 return 100 * LITRES_PER_GALLON / KMS_PER_MILE / mpg

print(convert_to_litres_per_100_km(32))
print(convert_to_litres_per_100_km(32.0))
#print(convert_to_litres_per_100_km(0))
