import random
import string

def generate_password():
    while True:
        try:
            length = int(input("Enter the length of your password: "))
            l = int(input("Do you want letters in your password? (If yes, enter 1 else enter 0): "))
            n = int(input("Do you want numbers in your password? (If yes, enter 1 else enter 0): "))
            s = int(input("Do you want symbols in your password? (If yes, enter 1 else enter 0): "))

            if l not in (0, 1) or n not in (0, 1) or s not in (0, 1):
                raise ValueError("Choices must be 1 (Yes) or 0 (No).")

            if l == 0 and n == 0 and s == 0:
                raise ValueError("You must choose at least one option (letters, numbers, or symbols).")

            return length, bool(l), bool(n), bool(s)

        except ValueError as ve:
            print(f"Invalid input: {ve}.\nPlease try again.")

password=''
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

if __name__ == '__main__':
    length, l, n ,s = generate_password()
    if l and n and s:
        choices = letters + numbers + symbols
    elif l and n:
        choices = letters + numbers
    elif l and s:
        choices = letters + symbols
    elif n and s:
        choices = numbers + symbols
    elif l:
        choices = letters
    elif n:
        choices = numbers
    else:
        choices = symbols

    for i in range(length):
        password += random.choice(choices)

    print(f"\nYour random generated password of length {length} is: {password}")
