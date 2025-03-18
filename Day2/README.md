# Error Classification
  - SyntaxError: Missing colon (:) in a for loop.
  - ZeroDivisionError: Division by zero in x = 10 / 0.
  - Logical Error: The calculate_area function mistakenly returns the circumference instead of the area of a circle.

# Debugging Complex Functions
  - ValueError: The function tries to convert the string 'abc' to an integer, which will cause an error.
  - SyntaxError: The print statement is missing a closing parenthesis.
  - Potential ZeroDivisionError: If data is an empty list, len(data) would be 0, leading to a division by zero.

# Advanced Debugging Challenge
  - The function randomly selects a number from [0, 1, 2], but if 0 is chosen, a ZeroDivisionError occurs because 10 / 0 is undefined.

# Writing Debug-Friendly Code
  -  The issue in the code is that '10%' is a string, not a number. The function expects discount to be an int or float, but receives '10%', causing a TypeError during arithmetic operations.

# Rubber Duck Debugging

 ## Creating a List
  - numbers = [1, 2, 3, 4, 5]
  - We create a list called numbers that contains five values: [1, 2, 3, 4, 5].
  - A list is a collection of items that are stored in square brackets ([]).
 ## Initializing a Variable
  - result = 1
  - We create a variable named result and set its value to 1.
  - This variable will be used to store the product of all numbers in the list. 
 ## Looping Through the List
  - for num in numbers:
  - result *= num
  - This is a for loop that goes through each number in the numbers list one by one.
  - num represents the current number from the list during each loop cycle.
  - result *= num is shorthand for:
  - result = result * num
  - which means we multiply result by num and update result.
 ## Understanding the Loop Execution
 ## Printing the Final Result
   - print("Product:", result)
   - The print() function displays the final product of the numbers in the list.
   - Product: 120

# Silent Failures
  - The code does not raise an error because the try-except block catches the exception and silently ignores it.
  - Normally, dividing by zero (10 / 0) raises a ZeroDivisionError.
  - However, since except: catches all exceptions and contains pass, the program continues execution without interruption.
  As a result, print("No error detected!")