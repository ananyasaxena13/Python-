

class Banking:

    def __init__(self):
        self.balance =1000

    def withdrawal(self, withdraw_amount):
        if self.balance > withdraw_amount:
            self.balance -= withdraw_amount
            print(f"Withdrawal successful! Your new balance is: {self.balance}")

        else:
            print("Insufficient balance! Please try again.")

    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Deposit successful! Your new balance is: {self.balance}")

