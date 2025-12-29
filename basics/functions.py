def square_sum(num1, num2):
    return (num1 + num2) ** 2

print(square_sum(2,3))

def sum_of_even(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    # sum = [sum + num for num in numbers if num % 2 == 0]
    # res = [i.upper() for i in text.split() if len(i) > 5]
    return sum

print(sum_of_even([1,2,3,4]))

def intro(first_name="Human", last_name = "Kiran", country = "Space"):
    '''
    Docstring for intro : Introduction about you
    
    :param first_name: Your First Name
    :param last_name: Your Last Name
    :param country: Your Country
    '''
    print(f"My name is {first_name} {last_name}")
    print(f"I live in {country}")
    print("Bye!!!")

# print(divide(5,4)) positional argument
# print(divide(b = 5, a = 10)) keyword arguments
# print(divide(10, b = 5)) must pass positional arguments before keyword arguments

# Print the documentation of any function
print(print.__doc__)
print(abs.__doc__)
print(intro.__doc__)

# Pass multiple arguments *args
def sum_of_nums(*nums):
    return nums

print(sum_of_nums(1,2,3,4))

def build_profile(**things):
    print("Building profile")
    for i, j in things.items():
        print(f"{i} : {j}")

build_profile(name="Raghu", age=99, profession="SD", hobbies=["playing, dancing"])

def mixed_example(msg1, msg2, msg3="Message3", *args, **kwargs):
    print(msg1, msg2)
    print(args)
    print(kwargs)
    print(msg3)

mixed_example("Example1", "Example2",1,2,3, name="Alice", role="Student")

counter = 0
def increment():
    global counter
    counter = counter + 1
    print(f"Counter : {counter}")

increment()
increment()
increment()
print(f"Counter : {counter}")

print(pow(2,3,3)) # 2 ** 3 % 3
# for name, age in zip(names, ages):
    # print(name, age)

# Higher Order Functions(Map, Filter, Reduce)
# Map 
 
def square(x):
    return x ** 2

numbers = [1,2,3,4,5]
squared_nums = map(square, numbers)
print(list(squared_nums))

string_numbers = ["1", "2", "3", "4", "5"]
# li = [int(i) for i in string_numbers]
li = list(map(int, string_numbers))
print(li)

# Filter
def is_even(x):
    return x % 2 == 0

numbers = [1,2,3,4,5,6,6,7,8]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# Reduce
from functools import reduce
def add(x, y):
    return x + y

total = reduce(add, numbers, 100)
print(total)

# Lambda Functions or Expressions
def add(x, y):
    return x + y

add_lambda = lambda x, y : x + y
print(add_lambda(3,4))

# Functions that take another functions as arguments or return a function are called as higher order functions

celsius_temps = [0, 20, 30, 45, 56]
f_temps = list(map(lambda x : (x * 9/5) + 32, celsius_temps))
print(f_temps)

# Filter the string longer than 5 characters
words = ["peacock", "parrot", "cat", "elephant", "dog"]
res = list(filter(lambda word : len(word) > 5 , words))
print(res)

# Sorting
students = [('charlie', 72), ('alice', 78), ('bob', 99)]
print(sorted(students, reverse=True, key=lambda x : x[1]))

employees = [
    {'name' : 'john', 'salary' : 50000, 'bonus' : 5000},
    {'name' : 'jane', 'salary' : 60000, 'bonus' : 7000},
    {'name' : 'john', 'salary' : 45000, 'bonus' : 4000},
]

# In case of dictionary
print(list(map(lambda x : x['salary'] + x['bonus'], employees)))
 
# Function within a function
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(5))
