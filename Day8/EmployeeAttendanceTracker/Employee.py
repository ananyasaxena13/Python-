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
            
    def mark_attendance(self, emp_id):
        lastsevendate = date.today() - timedelta(days=7)
        for employee in self.employee_list:
            if employee['emp_id'] == emp_id:
                employee['attendance'] = []
                for i in range(7):
                    curr_date = lastsevendate + timedelta(days=i)
                    employee['attendance'].append()
                     


    def get_employee(self, name):
        for employee in self.employee_list:
            if employee['name'] == name:
                print(employee['emp_id'])

    def delete_employee(self, emp_id):
        self.employee_list = [employee for employee in self.employee_list if employee['emp_id'] != emp_id]
        print("Employee deleted successfully")


    

    