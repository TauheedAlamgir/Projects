#Tauheed Alamgir 101194927

def replicate(s: str) -> str:
 """ 
 Replicates the string data of s multiplied by how many characters is in s.
 >>> rep = replicate('grrrrt')
 'grrrrtgrrrrtgrrrrtgrrrrtgrrrrtgrrrrt'
 >>> rep = replicate('wooback')
 'woobackwoobackwoobackwoobackwoobackwoobackwooback'
 >>> rep = replicate('peakaboo')
 'peakaboopeakaboopeakaboopeakaboopeakaboopeakaboopeakaboopeakaboo'
 >>> rep = replicate('Iwant')
 'IwantIwantIwantIwantIwant'
 >>> rep = replicate('100pls')
 '100pls100pls100pls100pls100pls100pls'
 """
 return s * len(s) 

rep = replicate('grrrrt')
print(rep)
rep = replicate('wooback')
print(rep)
rep = replicate('peakaboo')
print(rep)
rep = replicate('Iwant')
print(rep)
rep = replicate('100pls')
print(rep)