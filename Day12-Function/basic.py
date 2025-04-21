def welcome():
    print("Welcome to Python!")

for i in range(3):
    welcome()




def square(n):
    return n * n




def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    



def full_name(first,last):
    return first + " " + last




def circle_area(radius):
    pi = 3.14
    return pi * radius * radius