"""
Program to create multiple objects from a class dynamically with unique object names
"""

# ============================================================================
# APPROACH 1: Using a Dictionary (Most Recommended)
# ============================================================================

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


# Create objects dynamically using dictionary
students_data = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 19, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A+"},
    {"name": "Diana", "age": 20, "grade": "B+"},
]

# Method 1: Create objects and store in dictionary
students = {}
for i, data in enumerate(students_data):
    obj_name = f"student_{i+1}"
    students[obj_name] = Student(data["name"], data["age"], data["grade"])

print("=" * 60)
print("APPROACH 1: Dictionary Storage (Recommended)")
print("=" * 60)
for key, obj in students.items():
    print(f"{key}: {obj.display_info()}")


# ============================================================================
# APPROACH 2: Using setattr() with a Class Namespace
# ============================================================================

class StudentManager:
    """Manager class to hold student objects as attributes"""
    pass

manager = StudentManager()

print("\n" + "=" * 60)
print("APPROACH 2: Using setattr() with Class Namespace")
print("=" * 60)

for i, data in enumerate(students_data):
    obj_name = f"student_{i+1}"
    student_obj = Student(data["name"], data["age"], data["grade"])
    setattr(manager, obj_name, student_obj)

# Access objects
for i in range(1, 5):
    obj_name = f"student_{i}"
    student = getattr(manager, obj_name)
    print(f"{obj_name}: {student.display_info()}")


# ============================================================================
# APPROACH 3: Using globals() (Use with Caution)
# ============================================================================

print("\n" + "=" * 60)
print("APPROACH 3: Using globals() (Not Recommended)")
print("=" * 60)

for i, data in enumerate(students_data):
    obj_name = f"student_{i+1}"
    globals()[obj_name] = Student(data["name"], data["age"], data["grade"])

# Access objects
print(f"student_1: {student_1.display_info()}")
print(f"student_2: {student_2.display_info()}")
print(f"student_3: {student_3.display_info()}")
print(f"student_4: {student_4.display_info()}")


# ============================================================================
# APPROACH 4: Using exec() (Most Powerful but Requires Caution)
# ============================================================================

print("\n" + "=" * 60)
print("APPROACH 4: Using exec() (Advanced)")
print("=" * 60)

namespace = {}
for i, data in enumerate(students_data):
    obj_name = f"student_{i+1}"
    student_obj = Student(data["name"], data["age"], data["grade"])
    namespace[obj_name] = student_obj

for key, obj in namespace.items():
    print(f"{key}: {obj.display_info()}")


# ============================================================================
# PRACTICAL EXAMPLE: Factory Function
# ============================================================================

print("\n" + "=" * 60)
print("APPROACH 5: Factory Function (Best Practice)")
print("=" * 60)

class StudentFactory:
    def __init__(self):
        self.students = {}
    
    def create_student(self, name, age, grade, obj_id=None):
        """Create a student object dynamically"""
        if obj_id is None:
            obj_id = len(self.students) + 1
        
        obj_name = f"student_{obj_id}"
        self.students[obj_name] = Student(name, age, grade)
        return obj_name
    
    def get_student(self, obj_name):
        """Retrieve a student by object name"""
        return self.students.get(obj_name)
    
    def list_all_students(self):
        """List all created students"""
        for obj_name, student in self.students.items():
            print(f"{obj_name}: {student.display_info()}")


# Usage
factory = StudentFactory()

for data in students_data:
    factory.create_student(data["name"], data["age"], data["grade"])

factory.list_all_students()

# Retrieve a specific student
student = factory.get_student("student_2")
print(f"\nRetrieved: {student.display_info()}")


# ============================================================================
# BONUS: Dynamic Object Creation with Automatic Naming
# ============================================================================

print("\n" + "=" * 60)
print("BONUS: Auto-naming with Counter")
print("=" * 60)

from itertools import count

class AutoNamedStudent:
    """Student class with automatic naming"""
    _counter = count(1)
    _instances = {}
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.id = next(self._counter)
        self.obj_name = f"student_{self.id}"
        AutoNamedStudent._instances[self.obj_name] = self
    
    def display_info(self):
        return f"[{self.obj_name}] Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    @classmethod
    def get_all_instances(cls):
        return cls._instances

# Create objects
auto_student1 = AutoNamedStudent("Eve", 20, "A")
auto_student2 = AutoNamedStudent("Frank", 19, "B")
auto_student3 = AutoNamedStudent("Grace", 21, "A+")

for obj_name, obj in AutoNamedStudent.get_all_instances().items():
    print(f"{obj_name}: {obj.display_info()}")
