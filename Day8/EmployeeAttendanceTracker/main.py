import Employee

employee = Employee.Employee()



while(True):
    print("1. Creating Employee")
    print("2. View Employee")
    print("3. Mark Attendance")
    print("4. Get Employee ID")
    print("5. Delete Employee")
    print("6. Report")
    print("7. Exit")
    user_choice = int(input("Enter your choice: "))



    if user_choice == 1:

        employee_name = input("Enter employee name")
        employee_age = int(input("Enter your age"))
        employee.create_employee(employee_name, employee_age)

    elif user_choice == 2:
        employee.display_employee_all()

    elif user_choice == 3:
        emp_id = int(input("Enter employee id who is present: "))
        employee.mark_attendance(emp_id)

    elif user_choice == 4:
        employee_name = input("Enter employee name to get the id")
        employee.get_employee(employee_name)

    elif user_choice == 5:
        emp_id = input("Enter employee id to be deleted")
        employee.delete_employee(emp_id)

    elif user_choice == 6:
        employee.report()

    elif user_choice == 7:
        user_active = False
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
    