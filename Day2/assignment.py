#Answers of the Assignment

##Error Classification

for i in range(5):
    print(i)
#Syntax Error : Missing colon at the end of the line

x = 10 / 0 
#ZeroDivisionError : Division by zero (Runtime Error) to avoid this error we will use try except block
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")

def calculate_area(radius):
    return 2 * 3.14 * radius 
#Logic Error : Formula to calculate area of circle is wrong, it should be 
    return 3.14 * radius * radius



## Debugging Complex Functions

def process_data(data):
    total = 0
    count = 0
    for item in data:
        total += int(item)  
#ValueError : invalid literal for int(): 'abc' to avoid
        try:
            total += int(item) 
            count += 1
        except ValueError:
            print("Invalid literal for int()")
    if(count ==0): # to avoid zerodevision error for string 
        return "Error: No valid data found in the list"
    return total / count
print(process_data(['10', '20', 'abc', '30']))


## Advanced Debugging Challenge
import random

def unreliable_function():
    number = random.choice([0, 1, 2])
    return 10 / number 
    # ZeroDivisionError : Division by zero to avoid we use try except block
    try:
        number = random.choice([0, 1, 2])
        return 10/number
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
for i in range(10):
    print(unreliable_function())


## Writing Debug-Friendly Code
    
def calculate_discount(price, discount):
    if isinstance(discount, str): # to avoid error we will check if discount is string or not
        discount = int(discount.strip('%'))
    return price - (price * discount / 100)

print(calculate_discount(100, '10%')) # TypeError: 10% is a string, not an integer 

## Rubber Duck Debugging


numbers = [1, 2, 3, 4, 5]   # at this line a list is defined with reference numbers
result = 1  # a variable result is defined with value 1
for num in numbers:     # a for loop is defined to iterate over numbers
    result *= num   # result is multiplied by num and stored in result
print("Product:", result)   # print the result


## Advanced Challenge: Debug a Multi-threaded Program

# Race Condition: when multiple threads concurrently access and modify a shared variable (counter in this case) without proper synchronization, leading to unpredictable and incorrect results.
#using threading.Lock
import threading

counter = 0
lock = threading.Lock() # Create a lock object

def increment():
    global counter
    for _ in range(100000):
        with lock: # Acquire the lock
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)] # _ is used as a throwaway variable
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # Expected: 200000


## Activity: Debug with Breakpoints

def divide(a, b):
    if b == 0: # to avoid zerodivision error we will check if b is zero or not
        return "Error: Cannot divide by zero!"
    result = a / b # for breakpoint code will pause at this statement and we can check the value of a and b
    return result

a = 10
b = 0 
print(divide(a, b))


## Memory Leaks and Performance Debugging

import time

def inefficient_function():
    result = []
    for i in range(100000):
        result.append(i * 2)
    time.sleep(2)
    return result

print(len(inefficient_function()))

# Optimize Code to Improve Performance using generator or list comprehension making the list and then adding to it index

import time

def efficient_function():
    for i in range(100000):
        yield i * 2  # Yield values one by one instead of storing them all

# Process the values efficiently without storing them all in memory
count = sum(1 for _ in efficient_function())

time.sleep(2)  # Simulate delay (if needed)
print("Count:", count)  # Output: 100000


# Unexpected None

def add(a, b):
    result = a + b # to avoid none we will return result
print(add(3, 4)) # function returns none because it does not return anything


# Silent Failures

try:
    result = 10 / 0  #zerodivision error occurs here
except:
    pass #silently ignores all exceptions to avoid we will print the error
print("No error detected!")