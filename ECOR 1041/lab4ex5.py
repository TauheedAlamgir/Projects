#Tauheed Alamgir 101194927

def repeat(s: str, n: int) -> str:
 """ 
 Return s repeated n times; if n is negative, return the
 empty string.
 >>> repeat('yes', 4)
 'yesyesyesyes'
 >>> repeat('no', 0)
 ''
 >>> repeat('no', -2)
 ''
 >>> repeat('yesnomaybe', 3)
 'yesnomaybeyesnomaybeyesnomaybe'
 """
 return s * n

rep = repeat('yes', 4)
print(rep)
rep = repeat('no', 0)
print(rep)
rep = repeat('no', -2)
print(rep)
rep = repeat('yesnomaybe', 3)
print(rep)
