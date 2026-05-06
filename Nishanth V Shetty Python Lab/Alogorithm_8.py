import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*"

    all_chars = letters + digits + symbols
    password = ""

    for _ in range(length):
        password += random.choice(all_chars)

    return password

def main():
    print("Password Generator")
    length = int(input("Enter password length: "))

    if length < 4:
        print("Length should be at least 4")
        return

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
