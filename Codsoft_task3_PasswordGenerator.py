import random
import string
print("Welcome to Password Generator")

def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password using random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    # Get password length from user
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4.")
    else:
        # Generate and display password
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number for the length.")