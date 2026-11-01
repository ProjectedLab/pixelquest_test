import random
import string

def generate_password():
    print("--- Secure Password Generator ---")
    
    # Get user input for password length
    try:
        length = int(input("Enter desired password length (minimum 6): "))
        if length < 6:
            print("Length too short! Setting minimum length to 6.")
            length = 6
    except ValueError:
        print("Invalid input! Defaulting to length of 12.")
        length = 12

    # Define the characters to use
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character pools
    all_chars = lower + upper + digits + symbols

    # Ensure at least one of each character type is included for strength
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle the list to make it truly random
    random.shuffle(password)

    # Convert list to string
    final_password = "".join(password)

    print("\nYour secure password is:")
    print(f"👉 {final_password}\n")

if __name__ == "__main__":
    generate_password()
