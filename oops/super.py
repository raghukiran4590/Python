class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Name: {self.name}, Position: {self.position}"

class Programmer(Employee):
    def __init__(self, name, position, programming_language):
        super().__init__(name, position)
        self.programming_language = programming_language

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Programming Language: {self.programming_language}"
    
employee = Employee("Alice", "Manager")
programmer = Programmer("Bob", "Developer", "Python")

print(employee.get_details())
print(programmer.get_details())
# ============================================================================
