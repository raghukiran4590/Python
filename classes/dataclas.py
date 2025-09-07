from dataclasses import dataclass

@dataclass
class Project:
    name: str
    payment: int
    client: str

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

p = Project("Django", 12500, "Anthem")
e = Employee("Raghu", 35, 75000, p)

print(p)

