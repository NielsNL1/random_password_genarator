import random
import string
import time
import pyperclip

# Ask the user for the number of characters they want in their password and how many passwords they want
how_many_characters = int(input("How many characters do you want your password to have? (only type the number): "))
how_many_passwords = int(input("How many passwords do you want? (only type the number): "))

# Function to generate a password
def generate_password():
    # Possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(how_many_characters))
    return password

# Generate and print the random password(s)
for i in range(how_many_passwords):
    password = generate_password()
    print(f"Password: {password}")
    pyperclip.copy(password)
    print("Password copied to clipboard!")

# Countdown
print("Closing in:")
for i in range(30, 0, -1):
    print(i, end='\r')
    time.sleep(1)
