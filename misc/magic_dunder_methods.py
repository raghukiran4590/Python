class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f"Employee(name={self.name}, position={self.position})"

    def __str__(self):
        return f"{self.name} holds the position of {self.position}"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.position == other.position
        return False

    def __len__(self):
        return len(self.name) + len(self.position)
    
    def __call__(self, *args, **kwds):
        return f"Employee {self.name} can be called like a function!"
    
    