from datetime import date, timedelta

class Employee:

    employee_list = []
    count = 100

    def create_employee(self, name, age):
        self.count += 1
        employee = {
            "emp_id": self.count,
            "name": name,
            "age": age,
        }
        print("Employee created successfully, employee id: ", employee['emp_id'])
        self.employee_list.append(employee)


    def display_employee_all(self):
        for employee in self.employee_list:
            if not employee:
                print("No employee found")
                return
            print(f"emp_id: {employee['emp_id']}, name: {employee['name']}, age: {employee['age']}")

    def get_employee(self, name):
        for employee in self.employee_list:
            if employee['name'] == name:
                print(employee['emp_id'])
            
    def mark_attendance(self, emp_id):
        last_seven_date = date.today() - timedelta(days=7)
        for employee in self.employee_list:
            if employee['emp_id'] == emp_id:
                if 'attendance' not in employee:
                    employee['attendance'] = []
                emp_attendance = employee['attendance']
                
                for i in range(7):
                    current_date = last_seven_date + timedelta(days=i)
                    attendance = input(f"Enter the attendance for {current_date}: , 'P' for present and 'A' for absent:").strip().lower()
                    employee_attendance = {
                        'date': current_date,
                        'attendance': attendance
                    }
                    emp_attendance.append(employee_attendance)
                print(emp_attendance)
                print("Attendance marked")


    def report(self):
        for employee in self.employee_list:
            print(f"Attendance report for :: emp_id: {employee['emp_id']}, name: {employee['name']}, age: {employee['age']}")
            if 'attendance' in employee:
                for i in employee['attendance']:
                    print(f"Date: {i['date']}, Attendance: {i['attendance']}")
            else:
                print("No attendance found for this employee")
                     

    

    def delete_employee(self, emp_id):
        self.employee_list = [employee for employee in self.employee_list if employee['emp_id'] != emp_id]
        
        print("Employee deleted")


    

    