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