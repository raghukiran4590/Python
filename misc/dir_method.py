# Dir method
x = [1,2,3]
print(dir(x))
print(x.__add__)

# __dict__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
person = Person("Alice", 30)
print(person.__dict__)

# Help method
print(help(person))