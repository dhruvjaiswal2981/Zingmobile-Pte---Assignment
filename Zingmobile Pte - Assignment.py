import re

# 1. Decimal to Hexa, Hexa to Decimal conversion
def decimal_to_hex(decimal):
    hex_chars = "0123456789ABCDEF"
    if not decimal.isdigit():
        print("Invalid input!")
        return
    decimal = int(decimal)
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        decimal //= 16
    print(hexadecimal)

def hex_to_decimal(hexadecimal):
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    power = len(hexadecimal) - 1
    for digit in hexadecimal:
        if digit.upper() not in hex_chars:
            print("Invalid input!")
            return
        decimal += hex_chars.index(digit.upper()) * (16 ** power)
        power -= 1
    print(decimal)

# 2. Maskify user mobile number
def maskify(number):
    masked = '#' * (len(number) - 3) + number[-3:]
    print(masked)

# 3. OOPS
class Person:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")
        self.mobile = input("Enter mobile number: ")
    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile)

# 4. Validate the Password
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[_@$]", password):
        return False
    return True

# Test functions
decimal_to_hex("255")      # Output: FF
hex_to_decimal("FF")       # Output: 255
maskify("9988776655")      # Output: #######655
person = Person()          # Interactive input for Person class
person.display()           # Display Person information
password = "Test@123"
if validate_password(password):
    print("Password is safe")
else:
    print("Password is not safe")
