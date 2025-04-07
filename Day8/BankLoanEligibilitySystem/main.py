import Bank

bank = Bank.Bank()

while(True):

    print("Let us check your loan eligibility")
    salary = int(input("Enter your salary: "))
    age = int(input("Enter your age: "))
    credit_score = int(input("Enter your credit score: "))

    bank.check_loan_eligibility(salary, age, credit_score)
    break