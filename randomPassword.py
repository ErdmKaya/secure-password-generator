import secrets
import string
import time

def generate_strong_password(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        has_digit = any(char.isdigit() for char in password)
        has_symbol = any(char in string.punctuation for char in password)
        
        if (use_digits and not has_digit) or (use_symbols and not has_symbol):
            continue
        return password

def get_yes_no(prompt):
    while True:
        choice = input(f"{prompt} (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

# Main
print("=======================================")
print("ADVANCED SECURE PASSWORD GENERATOR")
print("=======================================")
print("Tip: Including numbers and symbols is recommended for strong security.\n") 


while True:
    try:
        user_input = input("Password Length (min 4): ")
        length = int(user_input)
        
        if length < 4:
            print("...Too short! Please enter at least 4 characters.")
            print("...Let's try again...\n")
        else:
            break 
            
    except ValueError:
        print("Invalid input! Please enter a number (e.g., 8, 12).")

include_digits = get_yes_no("Include numbers?")
include_symbols = get_yes_no("Include symbols?")

print("\nGenerating secure password...")
time.sleep(1)

password = generate_strong_password(length, include_digits, include_symbols)

print("-" * 30)
print(f"YOUR PASSWORD: {password}") 
print("-" * 30)
print("Do not share your password with anyone!")