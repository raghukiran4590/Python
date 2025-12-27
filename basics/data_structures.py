fruits = ['apple', 'banana', 'orange', 'mango']
# for i in range(len(fruits)):
#     print(fruits[i])

# for i in fruits:
#     print(i)

print(list(enumerate(fruits)))

for index, fruit in enumerate(fruits):
    print(index, '->', fruits[index])

nums = [1,3,5,7,9, 10]

for num in nums:
    if num % 2 == 0:
        print("Even number found", num)
        break
else:
    print("No even numbers found")

# Collections

# String : Ordered, Immutable sequence of characters
# List : Ordered, Mutable sequence of mixed data types
# Tuple : Ordered, Immutable collection
# Dictionary: <3.7 Unordered ; >3.7 Insertion-Ordered Key-Value Pairs
# Set: Unordered Mutable Collection
# Frozenset: Unordered Immutable Collection



