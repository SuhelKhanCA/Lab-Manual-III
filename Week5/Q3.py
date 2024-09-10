# Generating a random password

import random
import string

def generate_random_password():
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_symbols = string.punctuation

    # Combine all characters
    all_characters = uppercase_letters + lowercase_letters + digits + special_symbols

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(10))
    return password

# Generate and print the password
random_password = generate_random_password()
print(f"Random password: {random_password}")
