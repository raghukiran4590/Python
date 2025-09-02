def read_acronym():
    look_up = input("What Acronym would you like to look up?\n")
    found = False
    try:
        with open("/Users/AF35861/Library/CloudStorage/OneDrive-ElevanceHealth/Desktop/input.txt") as file:
            for line in file:
                if look_up in line:
                    print(line)       
                    found = True
                    break
    except FileNotFoundError as e:
        print("File does not exist")
        return
    
    if not found:
        print("Acronym doesn't exist")

def add_acronym():
    acronym_input = input("Enter the acronym you would like to add?\n")
    definition_input = input("Enter acronym definition you would like to add?\n")
    with open("/Users/AF35861/Library/CloudStorage/OneDrive-ElevanceHealth/Desktop/input.txt", "a") as file:
        file.write("\n"+acronym_input + " - "+ definition_input)
    print("Acronym Added Successfully!")


def main():
    user_input = input("Would you like to read(R) from the file or write(W) into the file?\n")
    if user_input == 'R':
        read_acronym()
    elif user_input == 'W':
        add_acronym()
    else:
        print("Invalid Choice")

main()

