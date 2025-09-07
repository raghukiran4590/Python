from datetime import date

class Employee:
    minimum_wage = 1000

    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * percent/100

class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus):
        super().increase_salary(percent)
        self.salary += bonus
        return self.salary

class Tester(Employee):
    pass


employee1 = Tester("Raghu", 35, 55000)
# employee2 = Developer
employee1.increase_salary(20)
print(f"Employee {employee1.name} earns a salary of {employee1.salary}")

employee2 = Developer("Vriha", 5, 89000, "Django")
employee2.increase_salary(30, 5000)
print(f"Employee {employee2.name} earns a salary of {employee2.salary}")

# print(Employee.__dict__)
Employee.__dict__["increase_salary"](employee1, 10)
print(f"Employee {employee1.name} earns a salary of {employee1.salary}")

print(Employee.minimum_wage)

print(date.today())
print(date.today().year, date.today().month, date.today().day)
print(date.today().year - 1990)
# print(date.today().year - 1990 - (date.today().month, date.today().day) < (10, 4))