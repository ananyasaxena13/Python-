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