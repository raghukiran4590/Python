import random

computer_choice = random.choice(["rock", "paper", "scissors"])
print(f"Computer chose: {computer_choice}")
user_choice = input("Do you want Rock, Paper or Scissors?\n")

if str(user_choice) == str(computer_choice):
    print("TIE")
elif str(computer_choice) == "scissors" and str(user_choice) == "rock":
    print("YOU WIN")
elif str(computer_choice) == "rock" and str(user_choice) == "paper":
    print("YOU WIN")
elif str(computer_choice) == "paper" and str(user_choice) == "scissors":
    print("YOU WIN")
else:
    print("YOU LOSE")