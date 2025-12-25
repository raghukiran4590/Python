a = 1
b = 2
c = 3

print(a, b, c)

d, e, f = 4, 5, 6
print(d, e, f, sep=", ")

# Unicode Character
print("\u0041")
print("\u0042")

# Unicode Character with Escape Sequence
print("\u0041\u0042")
print("\u0041\u0042\u0043")

print("\U0001F600")  # Unicode Character for a Grinning Face
print("\U0001F601")  # Unicode Character for a Grinning Face with Smiling Eyes

dir = "C:\\Users\\Public\\Documents"
print(dir) 

print(f"This is curly brace:{{")

print(f"This is curly brace:}}")

print(f"This is curly brace:{{}}")

star = "*"
print((star * 10) * 5)
print((star * 5) * 10)

print (a * -10)  # Output: -10
print(ord('A'))  # Output: 65

txt = 'Python Programming'
print(txt[0])  # Output: P
print(txt[::-1])  # Output: gnimmargorP nohtyP

print(txt.title())  # Output: Python Programming
print(txt.lower())  # Output: python programming
print(txt.upper())  # Output: PYTHON PROGRAMMING``
print(txt.capitalize())  # Output: Python programming
print(txt.swapcase())  # Output: pYTHON pROGRAMMING'
print(txt.isalpha())  # Output: False
print(txt.isalnum())  # Output: False
print(txt.islower())  # Output: False
print(txt.isupper())  # Output: False
print(txt.isspace())  # Output: False
print(txt.istitle())  # Output: True
print(txt.isdigit())  # Output: False
print(txt.isdecimal())  # Output: False
print(txt.isnumeric())  # Output: False
print(txt.isidentifier())  # Output: False
print(txt.isprintable())  # Output: True
print(txt.isascii())  # Output: True
print(txt.isascii())  # Output: True
print(txt.strip())
print(txt.lstrip())  # Output: Python Programming
print(txt.rstrip('P'))  # Output: Python Programming
print(txt.lstrip('P'))  # Output: ython Programming
print(txt.find('P'))  # Output: 0

# txt.isdigit('P Programming')  # Output: 10
print(txt.find('P', 1))  # Output: 10

# txt.isalnum('P Programming')  # Output: 10
print(txt.find('P', 1, 5))  # Output: 10

# txt.isalpha('P Programming')  # Output: 10
# print(txt.find('P', 1, 5, 10))  # Output

# isLower(), isUpper(), isSpace(), startsWith(), endsWith()
# isalpha(), isalnum(), islower(), isupper(), isspace(), istitle(), isdigit(), isdecimal(), isnumeric(), isidentifier(), isprintable(), isascii()
# strip(), lstrip(), rstrip(), find(), index(), replace(), split(), join(),
# format(), format_map(), rjust(), ljust(), center(), zfill(), expandtabs(), maketrans(), translate(), removeprefix(), removesuffix() 

# .format() method
print("The value of a is {} and the value of b is {}".format(a, b))
print("The value of a is {0} and the value of b is {1}".format(a, b))
print("The value of a is {1} and the value of b is {0}".format(a, b))
print("The value of a is {a} and the value of b is {b}".format(a=a, b=b))
print("The value of a is {a} and the value of b is {b}".format(a=1, b=2))

# s = "Hello"
# print(s[0])  # Output: H
# print("M" + s[1:])  # Output: Mello

# Raw String
print(r"C:\Users\Public\Documents")  # Output: C:\Users\Public\Documents
print(r"Hell\o")  # Output: Hell\o
print(r"Hello\nWorld")  # Output: Hello\nWorld
print(r"Hello\tWorld")  # Output: Hello\tWorld
print(r"Hello\bWorld")  # Output: Hello\bWorld
print(r"Hello\rWorld")  # Output: Hello\rWorld
print(r"Hello\fWorld")  # Output: Hello\fWorld

text = " python Programming SKILLS"
# strip, capitalize first letter, replace skills with expertise
print(text)
print(text.strip(" ").replace("SKILLS", "expertise"))
new_string = text.strip(" ").replace("SKILLS", "expertise").title()
print(new_string)


# Advanced Slicing Challenge
# Print every second character using slicing
# Print the string in reverse order using slicing
# Extract and print just "Programming" using negative slicing

s = "Python Programming Language"
print(s[-20:-9:])
print(s[::-1])
print(s[::2])

# String concatenation and slicing
# Create a new string by extracting the first letter of each word and concatenating them
str = "python is easy to learn"
print(str)
new_str = str.split(" ")
print(new_str[0][0] + new_str[1][0] + new_str[2][0] + new_str[3][0] + new_str[4][0])


# String Palindrome Check
text = "radar"
print(text == text[::-1])

# Count the occurrences
text = "Mississippi"
print(f"Count of occurrences of i : {text.count('i')}")
print("Count of occurrences of s : {}".format(text.count('s')))
print("Count of occurrences of p : {}".format(text.count('p')))