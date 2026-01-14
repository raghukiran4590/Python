class Person:

    def __init__(self, name = None, age = None, occupation = None, country = None):
        if name is None:
            name = "Rahul Sharma"
        if age is None:
            age = 30
        if occupation is None:
            occupation = "Doctor"
        if country is None:
            country = "India"
        
        self.name = name
        self.age = age
        self.occupation = occupation
        self.country = country
        print(f"Initialized Person: {self.name}, {self.age}, {self.occupation}, {self.country}")
    
# Example usage:
person = Person("John Doe", 30, "Engineer", "USA")
engineer = Person("Jane Smith", 28, "Software Developer", "Canada")
doctor = Person()


