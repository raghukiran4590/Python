import time

questions = ["what is the capital of France?", "what is 2 + 2?", "who wrote 'Hamlet'?", 
             "what is the largest planet in our solar system?", "what is the boiling point of water in Celsius?"]


answers = {
    0: "Paris",
    1: "4",
    2: "William Shakespeare",
    3: "Jupiter",
    4: "100"
}

amount = 0

print("Welcome to the Kaun Banega Crorepati game!\n")
for i, question in enumerate(questions):
    print(f"Computer Ji, display the question {i + 1} on the screen please : {question}\n")
    user_answer = input("Your answer: ")
    print("Are you sure about your answer? Think again!\n")
    time.sleep(2)
    if user_answer.strip().lower() == answers[i].strip().lower():
        print("Your answer is Correct!\n")
        amount += 100000 * (i + 1)
        print(f"Congratulations! You have won {amount} amount so far.\n")
    else:
        print("Shall i lock the answer? (yes/no)")
        time.sleep(3)
        print(f"Unfortunately, It is a wrong answer. The correct answer is: {answers[i]}")
        print(f"Sorry to see you go back, but you have won {amount} amount so far.")
        break
else:
    print("Congratulations! You have answered all the questions correctly.")
    print("You are the winner of the game and you have won one crore rupees!")





