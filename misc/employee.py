from magic_dunder_methods import Employee

emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")

print(repr(emp1))  # Output: Employee(name=Alice, position=Developer)
print(str(emp2))   # Output: Bob holds the position of Designer
print(emp1 == emp2)  # Output: False
print(len(emp1))   # Output: Length of the name and position combined

