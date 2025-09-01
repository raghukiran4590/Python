expenses = []
num_of_expenses = int(input("Enter the number of expensens:"))
for i in range(num_of_expenses):
    expenses.append(float(input("Enter the expense:")))

print(expenses)
# total = sum(expenses)
sum = 0
for x in expenses:
    sum = sum + x

print('You spent $', sum, sep='')
# print(f"You spent ${total}")