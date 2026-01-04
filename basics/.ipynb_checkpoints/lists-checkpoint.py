info = ["Alice", 30, 5.5, True]
li = list()

# print(type(info))
# print(type(li)) 

s = {10, 20, 30}
li = list(s)
print(li)
print(list(range(10)))

copied_list = list(li)
print(copied_list)

numbers = [10, 20, 30, 40, 50]
print(numbers[1:])
print(numbers[len(numbers)-1])
print(numbers[::-1])
print(numbers[:-4:-1])
print(numbers[-3::])

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)
fruits.insert(2, "grapes")
print(fruits)

fruits2 = ["orange", "blueberry"]
fruits.extend(fruits2)
print(fruits)

fruits.remove("banana")
fruits.pop()
print(fruits)

del fruits[1:3]
print(fruits)

fruits.clear()
print(fruits)

# Shallow Copy
a = [[1,2], [3,4]]
# b = a[:]
# b[0][0] = 99
# print(a)
# print(b)
# print(id(a[0]), id(b[0]))

# Deep Copy
import copy
b = copy.deepcopy(a)
print(id(a[0]), id(b[0]))
b[0][0] = 99
print(a)
print(b)

a = [1,2,3]
b = [4,5,7]
result = a + b
print(result)
print(result + [6])

fruits = ["apple", "banana", "orange"]
print("kiwi" in fruits)
print("kiwi" not in fruits)

names = ["Alice", "ALice", "Charlie"]
print(min(names))
print(max(names))
print(ord('l'), ord('L')) 

# list.sort(key = len, reverse = True)
# sorted_new_list = sorted(list, key = len, reverse = True)

reversed_list = []
for i in range(len(fruits)-1, -1, -1):
    reversed_list.append(fruits[i])
print(reversed_list)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# for row in matrix:
#     for x in row:
#         print(x, end=' ')
#     print()


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

good = []
li = [0,0,0]
for _ in range(3): # _ means loop variable never used
    good.append(li[:])
good[0][0] = 1
print(good)

a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)
b = a
print(a is b)

# List Comprehension
li = [1,2,3,4,5,6,7]
res = []

# for l in li:
#     res.append(i ** 2)

res = [i ** 2 for i in li] # [expression for i in list]
print(res)

res = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(res)

res = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]
print(res)

drinks = ["juice", "coffee"]
deserts = ["donut", "icecream", "cake"]
res = []
# for i in drinks:
#     for j in deserts:
#         res.append((i, j))
# print(res)

res = [(i, j) for i in drinks for j in deserts]
print(res)

text = "Python list comprehension is powerful and concise"
words = text.split()
res = []
for i in words:
    if len(i) > 5:
        res.append(i.upper())
print(res)

res = [i.upper() for i in text.split() if len(i) > 5]
print(res)

# Tuple 

t = (1, [2,3])
t[1].append(4)
print(t)

# a,b = 1,2,3 #unpacking error too many values to unpack
a, *b = 1,2,3
print(a)
print(b)

(a,b), (c,d), (e, f) = ((1,2), (3,4), (5,6))

colors = ('red', 'green', 'blue')
# for index, color in enumerate(colors):
for index, color in enumerate(colors, start=1):
    # print(t, type(t))
    print(index, color)
