class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        if self.x is None or self.y is None:
            raise NotImplementedError("Subclasses must implement this method")
        return self.x * self.y
    
class Rectangle(Shape):
    def area(self):
        return self.x * self.y

class Circle(Shape):
    def area(self):
        import math
        return math.pi * (self.x ** 2)  # Here, x is the radius
    
# Example usage:
rect = Rectangle(4, 5)
print("Rectangle Area:", rect.area())

circle = Circle(3, None)
print("Circle Area:", circle.area())

