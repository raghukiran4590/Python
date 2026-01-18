(a := False)
print(a)
b = True
print(b)
print(b := not a)


numbers = [1,2,3,4,5]

while (n := len(numbers)) > 0:
    # print(numbers.pop())
    numbers.pop()

print(n)
print(numbers)

# Food list

food = list()
while (item := input("Enter a food item (or 'quit' to stop): ")) != 'quit':
    food.append(item)

print("You entered:", food)
