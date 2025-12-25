salary = 10_00_000
print(salary)

binary_num = 0b1010101;
print(type(binary_num))
print(binary_num)

a = 10;
b = 3;
print(f"Power:{a ** b}")
print(f"Regular Division : {a / b}")
print(f"Integer Division : {a // b}")

electron_mass = 9.11e-31 # 9.11 x 10(to power of -31)
pi = 3.141578234
print(f"{pi:.2f}")

# bool is a Subclass of int
print(True == 1)
print(False == 0)
print(True + True)
print(False + True)
print(int(True))
print(int(False))

# Truthy and Falsy values
print(bool(1))
print(bool(0))

print(bool(0))
print(bool(0.0))
print(bool({}))
print(bool([]))
print(bool(None))

# Every Boolean is an integer
print(isinstance(True, int))
# Integers are not boolean
print(isinstance(1, bool))

print(True.bit_length())
print(False.bit_length())

has_injury = True
print(not has_injury)

score = 10
if score >= 10:
    pass
print("You need to study hard")

a,b,c = 10, 20, 30
print(a, b, c)

operation = input("Enter the operation : ")
result = a + b + c if operation == 'add' else c - b - a if operation == 'sub' else 'Unknown Operation'
print(result)


