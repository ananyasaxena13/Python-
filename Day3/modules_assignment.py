#Fix the circular import problem between module_a.py and module_b.py.

#module_a.py:

def func_a():
    return "Function A"
#to resolve the circular dependencies we will import module where we need it not at the top of the file
import module_b
print(module_b.func_b())

#module_b.py:
import module_a

def func_b():
    return "Function B"


#Dynamic Module Loading

import importlib

def dynamic_import_and_execute():
    module_name = input("Enter module name: ")
    function_name = input("Enter function name: ")
    argument = input("Enter argument: ")

    try:
        module = importlib.import_module(module_name)  # Dynamically import module
        func = getattr(module, function_name)  # Get function from module

        if callable(func):
            # Convert input to appropriate type (int, float, etc.)
            try:
                argument = eval(argument)
            except:
                pass  # Keep as string if eval fails

            result = func(argument)  # Execute function
            print("Output:", result)
        else:
            print(f"'{function_name}' is not a callable function in {module_name}.")
    except (ModuleNotFoundError, AttributeError) as e:
        print("Error:", e)

# Run the function
dynamic_import_and_execute()

#Dynamic Module Loading

#creating module calculator.py

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except TypeError:
        return "Error: Invalid data type"
    except Exception as e:
        return "Error: An unexpected error occurred"
#now for handling division by zero and invalid inputs we will use calculator.py module
#and use that module in mainCalci.py to handle exceptions
#importing calculator module to handle exceptions
import calculator

a = input("Enter first number: ")
b = input("Enter second number: ")

try:
    a, b = float(a), float(b)  # Convert input to float
    result = calculator.divide(a, b)
except ValueError:
    result = "Invalid input: Please enter numeric values."

print("Result:", result)

#Advanced Import Strategies

import importlib 

module_name = input("Enter module name: ")
function_name = input("Enter function name: ")
argument = input("Enter argument: ")
#taking inputs
def dynamic_function(module_name, function_name, argument):
    try:
        module = importlib.import_module(module_name) #importing module
        #check if the function exists
        func = getattr(module,function_name, None) 

        if callable(func):
            print("Output:", func(argument))
        else:
            print(f"'{function_name}' is not a callable function in {module_name}.")
    #handling errors for module and other errors
    except (ModuleNotFoundError, Exception) as e:
        print(f"Error: {e}")

dynamic_function(module_name, function_name, argument)


#Optimize Import Time

import time

# Importing single module
start = time.time()
import math
end = time.time()
print(f"Import time: {end- start:.6f} seconds")

# Importing everything from same module

start = time.time()
from math import *
end = time.time()
print(f"Import time: {end- start:.6f} seconds")

#Module Creation and Distribution

#customModule.py
import sys
#adding custom path of module 
sys.path.append(r"C:\Users\anasa\OneDrive\Desktop\Python-Training\Python-\Day3\Ques3")  # Add custom path

import calculator  # Now we can import it

print(calculator.divide(10, 2))  # Output: 5.0


