import Employee

employee = Employee.Employee()



while(True):
    print("1. Creating Employee")
    print("2. View Employee")
    print("3. Get Employee")
    print("4. Delete Employee")
    user_choice = int(input("Enter your choice: "))



    if user_choice == 1:

        employee_name = input("Enter employee name")
        employee_age = int(input("Enter your age"))
        employee.create_employee(employee_name, employee_age)

    elif user_choice == 2:
        employee.display_employee_all()

    elif user_choice == 3:
        employee_name = input("Enter employee name to get the id")
        employee.get_employee(employee_name)

    elif user_choice == 4:
        emp_id = input("Enter id of employee to be deleted")
        employee.delete_employee(emp_id)

    