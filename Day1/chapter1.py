#value and data Types
'''Write a program that:
     - Assigns different values to variables.
     - Prints the type of each variable
'''
x = 42 
y = 3.14
z = 'Hello'
print(type(x), type(y), type(z)) # <class 'int'> <class 'float'> <class 'str'>

#Operators and Operands
''' Create a Python script that demonstrates:
     - Addition, subtraction, multiplication, and division.
     - Comparisons between numbers.
     - Logical operations like `and`, `or`, `not`.'''

a = 10
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b) # 13 7 30 3.3333333333333335 3 1 1000
print(a > b, a < b, a == b, a != b) # True False False True
print(a > 5 and b < 5) # True

#Function Calls
'''Write a program that uses built-in functions inside expressions:'''

numbers = [5, 3, 8, 1]
print(max(numbers) - min(numbers)) # 7

'''Assign a function to a variable, then call the function using the new variable'''

greet = print
greet('Hello, World!') # Hello, World!

#Data Types
'''Create variables of different types and print their types'''

a = 10
b = 'Python'
c = 3.14
print(type(a), type(b), type(c))

#Type Conversion Functions
'''Convert variables between types and observe the results'''

num = '123'
converted_num = int(num) # 123
print(converted_num, type(converted_num)) # 123 <class 'int'>

#Variables
'''Assign values to variables, print them, and observe changes upon reassignment.'''

x = 5
print(x) # 5
x = 10
print(x)  # 10

#Variable Names and Keywords
'''Try using reserved keywords as variable names and observe the errors.'''

import keyword; 
print(keyword.kwlist) # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


