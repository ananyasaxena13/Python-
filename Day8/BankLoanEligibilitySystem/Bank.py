#Bank loan eligibility system
#based on salary, age, and credit score using nested conditionals.

class Bank:

    def check_loan_eligibility(self,salary, age, credit_score):
        if salary >= 25000:
            if age >= 21:
                if credit_score >= 700:
                    print("You are eligible for the loan")
                else:
                    print("You are not eligible for the loan. LOW CREDIT SCORE")
            else:
                print("You are not eligible for the loan. AGE must be above 21")
        else:
            print("You are not eligible for the loan. SALARY below ")
