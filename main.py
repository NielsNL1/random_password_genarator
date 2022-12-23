import random
import string

# asks user how many characters they want and how many passwords they want
how_many_characters = input('How many characters do you want it to have? (only type the number) ')
how_many_passwords = input('How many passwords do you want? (only type the number) ')

how_many_characters = int(how_many_characters)
how_many_passwords = int(how_many_passwords)


# defines generate_password
def generate_password():
    # Creates a las of the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generates a random password
    password = ''.join(random.choice(characters) for i in range(how_many_characters))

    # Return the generated password
    return password


# prints the random password
for i in range(how_many_passwords):
    print(generate_password())
