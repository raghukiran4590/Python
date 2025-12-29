d = {}

fruits = {
    "apple" : "red",
    "banana" : "yellow",
    "kiwi" : "brown"
}
print(fruits)

print(dict(orange = "orange", pineapple = "yellow"))

d = dict([('apple', 'red'), ('banana', 'yellow'), ('kiwi', 'brown')])
print(d)

# Internally dictionary is stored as HashTable
# HashTable is a special type of Array

index = hash("age") % 8
print(index)

print(d.get("apple"))
print(d["apple"])

# Python calculates with its internal algorithm to find the key-value in case of collision
mixed = {
    1 : "one",
    "two" : 2,
    (3,4) : "tuple as key"
}

print(mixed)

# Dictionary key cannot start with number, it should be the same as variable
person = {'name' : 'alice', 'age' : 25}
print(person['name'])
# print(person['names']) Gives Key error if the key is not found in the dictionary
print(person.get('names')) # Gives None if the key is not found
print(person.get('names','NA')) # Default can be set if the key does not exist

#  Dictionary Methods 
student = {'name' : 'alice', 'age' : 25, 'grade' : 'A'}
print(student.keys())
print(student.values())
print(student.items())

for key in student: # default student.keys()
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key} : {value}")

# Merge Operation Python 3.9+
a = {'a' : 1}
b = {'b' : 2}
a = a | b
# a |= b
print(a)

print(a.get('c', 'NA'))
print(a.setdefault('c', 123))

# Dictionary Comprehension
# {key_expression: value_expression for item in iterable if condition}

res = {}
res = {i:i**2 if i % 2 ==0 else i ** 3 for i in range(1, 11)}
print(res)

# Multiplication table of 5
res = {i : {j : i*j for j in range(1, 11)} for i in range(1,6)}
print(res)

# Sets - Unordered, Unindexed, mutable, unique
# Used in Mathematical operations union, intersection, difference
# fast membership testing
# Cannot store lists in Sets

mixed = {1, "hello", 3.14, True}
print(mixed)

# Empty Set
# e = {} This creates a empty dictionary not a set
e = set()
print(e)
print(type(e))
print(len(e))

print(set([1,2,3,4,5,2,1,2]))
print(set("hello"))
print(set((1,2,3,4,2,1,1)))
print(set(range(1,10)))

# Set Operations
# add() -> add only one iterable item at a time (excpet lists)
# update() -> add multiple elements including lists
# add("abc") adds as one string ; update("abc") adds each character as one element

# remove(), discard(), pop(), clear()

# Mathematical Set Operations
set_a = {1,2,3,4}
set_b = {3,4,5,6}
union_result1 = set_a | set_b
print(union_result1)
print(set_a.union(set_b))

union_with_list = union_result1.union([3,2,1])
print(union_with_list)

set_a = {1,2,3,4}
set_b = {3,4,5,6}
intersection_result1 = set_a & set_b
print(intersection_result1)

set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9}
print(set_b - set_a)
print(set_a.difference(set_b))

set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9}
symmetric_difference_result = set_a ^ set_b
print(symmetric_difference_result)
print(set_a.symmetric_difference(set_b))

# Match-Case Statement
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(404))
# Output: Not found
print(http_error(500))
# Output: Something's wrong with the internet

def get_day_name(day_number):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    # Use .get() to provide a default value if the key is not found
    return switcher.get(day_number, "Unknown day") 

print(get_day_name(4))
# Output: Thursday
print(get_day_name(8))
# Output: Unknown day
