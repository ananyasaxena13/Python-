import Banking

banking = Banking.Banking()

while True:
    print("Welcome to the ATM!")
    print("1. Check Balance")
    print("2. Withdrawal Money")
    print("3. Deposit Money")
    print("4. Exit")
    user_choice = int(input("Please enter your choice: "))

    if user_choice == 1:
        print(f"Your current balance is: {banking.balance}")

    elif user_choice == 2:
        withdraw_amount = int(input("Enter amount to withdraw: "))
        banking.withdrawal(withdraw_amount)

    elif user_choice == 3:
        deposit_amount = int(input("Enter amount to be deposit: "))
        banking.deposit(deposit_amount)

    elif user_choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")