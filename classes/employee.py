class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_pay):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_pay = hourly_pay
    
    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_pay

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, number_of_sales, commission_rate):
        super().__init__(fname, lname, salary)
        self.number_of_sales = number_of_sales
        self.commission_rate = commission_rate
    
    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.number_of_sales*self.commission_rate
        return regular_salary + total_commission
    


 

    

    


        