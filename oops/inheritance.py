class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def display_info(self):
        return f"Employee ID: {self.id}, Name: {self.name}"
    
class Programmer(Employee):
    def __init__(self, id, name, language):
        super().__init__(id, name)
        self.language = language
    
    def display_programmer_info(self):
        base_info = super().display_info()
        return f"{base_info}, Language: {self.language}"

class Manager(Employee):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department
    
    def display_manager_info(self):
        base_info = super().display_info()
        return f"{base_info}, Department: {self.department}"

employee = Employee(1, "Alice")
programmer = Programmer(2, "Bob", "Python")
manager = Manager(3, "Charlie", "HR")

print(employee.display_info())
print(programmer.display_info())
print(programmer.display_programmer_info())
print(manager.display_info())
print(manager.display_manager_info())


# ============================================================================

# Access Modifiers Example

class Base:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private" # Name Mangling

    def display_vars(self):
        return (self.public_var, self._protected_var, self.__private_var)

class Derived(Base):
    def access_vars(self):
        public = self.public_var
        protected = self._protected_var
        # private = self.__private_var  # This will raise an AttributeError
        return (public, protected)
    
base = Base()
derived = Derived()
print(base.display_vars())
print(derived.access_vars())
print(base._Base__private_var)  # Accessing private variable using name mangling
print(derived._Base__private_var)  # Accessing private variable from derived class using name mangling
print(base._protected_var)  # Accessing protected variable from outside (not recommended)
# ============================================================================




        
