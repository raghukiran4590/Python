contacts = {
    "number" : 4,
    "students" : [
        {"Name":"Sarah Holderness", "Email":"sarah@example.com"},
        {"Name":"Harry Potter","Email":"harrypotter@example.com"},
        {"Name":"Mike Clarke", "Email":"mikeclarke@example.com"},
        {"Name":"Brian Lara", "Email":"blara@example.com"}
    ]
}

# print(contacts["students"])
print("Student Emails :")
for student in contacts["students"]:
    print(student['Email'])

