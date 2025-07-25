import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short! Minimum length is 4."

    # Combine all character types
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Password Generator 🔐")
length = int(input("Enter desired password length: "))

password = generate_password(length)
print(f"\nGenerated Password: {password}")