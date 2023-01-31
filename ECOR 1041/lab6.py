# Tauheed Alamgir 101194927
#ECOR 1041 Lab 6 Solution Template
#
#Author: Tauheed Alamgir 101194927
#
#This file is to be used in conjunction with the detailed lab description for 
# Lab 6
#Use this file to enter your answers to the series of exercises you will 
# complete.
#
#==========
#
#Exercise 1: Single or Double Quotes - Does it matter? Yes, it does matter. 
#
#Example, "haven't" or '"Spam, spam, spam," he said.'
#
#>>> type('Hello')
# Type what you see: <class 'str'>
#
#>>> type("goodbye")
# Type what you see: <class 'str'>
#
#>>> 'Hello'
# Type what you see: 'Hello'
#
#>>> ""     (An empty string - type two quotes with no spaces between them.)
#'' we see two single quotation marks.
#
#>>> '"Spam, spam, spam," he said.'
# Type what you see: (Nested quotations) '"Spam, spam, spam," he said.'
#
#>>> "I haven't a clue" 
# Type what you see: (Nested apostrophe) "I haven't a clue"
#
#>>> 'I haven't a clue' 
# Type what you see: (Nested apostrophe) 
#Traceback (most recent call last):
#  Python Shell, prompt 7, line 1
#Syntax Error: invalid syntax: <string>, line 1, pos 10
#
#
#Concluding Questions: Generally, either double or single quotes works well but
# can you give a scenario where one is better than the other?
# It is better to use double quotes when there is a word that has a quotation 
# mark in it already like for example in our exercise the word
# haven't has a quotation mark so the program thinks thats the end of the line. 
# In other words if your line already has single quotation
# marks then you use double quotation marks and vice versa.
#==================
#
#Exercise 2: What operations are permitted with values of type str? It is + and
# *.
#
#When used with strings, + is the concatenation operator. 
#
#>>> 'Hello, ' + 'world!'
# Type what you see: 'Hello, world!'
#
#When used with strings, * is the replication operator.
#
#>>> "Spam" * 3
# Type what you see: 'SpamSpamSpam'
#
#>>> 3 * "Spam"
# Type what you see: 'SpamSpamSpam' (Reflect: What does this say about order of
# operators?) The order of operators do not matter as you can
#see in our example above you can place it before or after as long as it is in
# between the operands.
#
#>>> "Spam" * 0
# Type what you see: ''
#
#>>> "Spam" * -3
# Type what you see: ''
#
#There are other operators to try now: - and /
#
#>>> "Hello" - "He"
# Type what you see: 
#Traceback (most recent call last):
#  Python Shell, prompt 13, line 1
#builtins.TypeError: unsupported operand type(s) for -: 'str' and 'str'
#
#
#>>> 'Spam' / 3
# Type what you see: 
#Traceback (most recent call last):
#  Python Shell, prompt 14, line 1
#builtins.TypeError: unsupported operand type(s) for /: 'str' and 'int'
#
#
#Concluding Questions: What operators work with strings?  Does the order of
# operands matter? Strings only work with two operators which
#are + and * while with - and / we get errors. No, as you can you can change 
# the order of the operands and still get an answer.
#
#
#=======================
#
#Exercise 3 : Understand the string representation
#
#Is  the string '123' the same as the integer 123? No, the string '123' gives
# us '123' while integer 123 gives 123.
#
#>>> '123' + 456 
#Traceback (most recent call last):
#  Python Shell, prompt 23, line 1
#builtins.TypeError: can only concatenate str (not "int") to str
#
#>>> '123' + '456'
#'123456'
#Concluding Question: When a string looks like a number, is it a number or a 
# string? 
#It is string.
#
#=========
#Last edited: August 18, 2020


#Ex 4
def repeat(s: str, n: int) -> str:
 """ Return s repeated n times; if n is negative, return the
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

#Ex 5
def total_length(s1: str, s2: str) -> int:
 """ Return the sum of the lengths of s1 and s2.
 >>> total_length('yes', 'no')
 5
 >>> total_length('yes', '')
 3
 >>> total_length('YES!!!!', 'Noooooo')
 14
 """
 return len(s1) + len(s2)

#Ex 6
def replicate(t: str) -> str:
 """ Replicate the string data of t according to how many digits t has.
 >>> replicate('the')
 'thethethe'
 >>> replicate('woo')
 'woowoowoo'
 >>> replicate('onetwo')
 'onetwoonetwoonetwoonetwoonetwoonetwo'
 >>> replicate('aaaaaa')
 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
 """
 return t * len(t) 

#=========================================================================

# Main Script Ex 4
x = repeat('yes', 4)
print(x)
y = repeat('no', 0)
print(y)
z = repeat('no', -2)
print(z)
s = repeat('yesnomaybe', 3)
print(s)

# Main Script Ex 5
x = total_length('yes', 'no')
print(x)
y = total_length('yes', '')
print(y)
z = total_length('YES!!!!', 'Noooooo')
print(z)

# Main Script Ex 6
x = replicate('the')
print(x)
y = replicate('woo')
print(y)
z = replicate('onetwo')
print(z)
s = replicate('aaaaaa')
print(s)
