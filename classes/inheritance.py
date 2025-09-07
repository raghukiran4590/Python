class Employee:
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
