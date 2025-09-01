from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        for i in self.employees:
            print(i.fname, i.lname)
        print("____________________________________")
    
    def pay_employees(self):
        for i in self.employees:
            print(f"Paycheck for Employee: {i.fname},{i.lname}")
            print(f"${i.calculate_paycheck():,.2f}")
            print("___________________________________")

def main():
    my_company = Company()

    employee1 = SalaryEmployee("Sarah", "Hess", 50000)
    employee2 = HourlyEmployee("Lee", "Smith", 40, 50)
    employee3 = CommissionEmployee("Bob", "Brown", 45000, 200, 15)
    
    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)

    print("Current Employees:")
    my_company.display_employees()
    my_company.pay_employees()

main()
