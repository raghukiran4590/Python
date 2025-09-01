import random

roll = random.randint(1,6)
print("Random Dice Roll : "+str(roll))

user_roll = input("Enter you dice input:\n")

if int(user_roll) == int(roll):
    print("Both are same\n")
else:
    print("Both are not same\n")



