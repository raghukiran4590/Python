'''
Docstring for exercises.ex1
Create a python program greeting you by the hour
'''

import datetime

def greet_by_hour():

    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 17:
        return "Good Afternoon!"
    elif 17 <= current_hour < 21:
        return "Good Evening!"
    else:
        return "Good Night!"
    

if __name__ == "__main__":
    print(greet_by_hour())


