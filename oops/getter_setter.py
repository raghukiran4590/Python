class StudentClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def get_name(self, value):
        self.name = value
    
    @property
    def get_age(self):
        return self.age / 10
    
    @get_age.setter
    def get_age(self, value):
        self.age = value * 10
    
    
if __name__ == "__main__":
    student = StudentClass("Alice", 10)
    print(student.name)
    student.get_name = "Bob"
    print(student.name)
    print(student.age)
    
    student.get_age = 12
    print(student.age)
    print(student.get_age)
    student.get_age = 15
    print(student.age)
    print(student.age)
    print(student.get_age)
