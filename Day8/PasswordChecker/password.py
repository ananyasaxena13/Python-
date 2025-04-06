import re

def check_password(password):
    score =0

    if len(password) >= 8:
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1

    if re.search(r'[a-z]', password):
        score += 1
    
    if re.search(r'[0-9]', password):
        score += 1

    if re.search(r'[@$!%*?&]', password):
        score += 1


    if score <3:
        print("Weak password")

    elif score < 5:
        print("Medium password")

    else:
        print("Strong password")

while True:
    password = input("Enter your password:")
    check_password(password)
    
