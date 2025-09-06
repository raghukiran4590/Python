class Employee:

    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None
    
    @property # Getter Decorator
    def salary(self):
        return self.__salary
    
    @salary.setter #Setter Decorator
    def salary(self, salary):
        if salary < 1000:
            raise ValueError("Minimum wage is $1000")
        self.__salary = salary
        self._annual_salary = None

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary =  self.salary * 12
            return self._annual_salary
    
    def __str__(self):
        return f"Employee: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}"
    def __repr__(self):
        return f"Employee('{self.name}', {self.age}, {self.salary}, '{self.position}')"

employee1 = Employee("Alice", 30, 70000, "Developer")
employee2 = Employee("Bob", 45, 90000, "Manager")

print(employee1)
print(employee2)

print(repr(employee1))
print(repr(employee2))

employee1.salary = 75000
employee2.salary = 95000

print(f"{employee1.name}'s new salary: {employee1.salary}")
print(f"{employee2.name}'s new salary: {employee2.salary}")

print(employee1.salary)  # This will raise an AttributeError
print(employee2.annual_salary)
employee2.salary = 1950
print(employee2.annual_salary)
# print(12 * 1950)

