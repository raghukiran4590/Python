class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"Hello, my name is {self.name}."

class Dance:
    def __init__(self, style):
        self.style = style

    def show(self):
        return f"I am dancing {self.style}."

class Dancer(Person, Dance):
    def __init__(self, name, style):
        self.name = name
        self.style = style
    
    # def __mro__(self):
    #     return [Dancer, Person, Dance, object]


o = Dancer("Alice", "Ballet")
print(o.show())  # Output: Hello, my name is Alice.
# The show method from Person is called due to method resolution order (MRO).
# To call the show method from Dance, we can use:
print(Dance.show(o))  # Output: I am dancing Ballet.
print(Dancer.__mro__)  # Output: (<class '__main__.Dancer'>, <class '__main__.Person'>, <class '__main__.Dance'>, <class 'object'>)