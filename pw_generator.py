import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    has_number = False
    has_special = False

    while len(pwd) < min_length or (numbers and not has_number) or (special_characters and not has_special):
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

    return pwd

def evaluate_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    unique_chars = len(set(password))

    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    if unique_chars >= length * 0.7:
        strength += 1

    return strength

print("🎉 Welcome to the Magical Password Generator! 🎩✨")
print("Answer a few questions and behold, your secret passphrase!")

min_length = int(input("First, how long would you like your magic word to be? (at least 6 characters): "))
while min_length < 6:
    print("Oh no! The magic word must be at least 6 characters long! ✨✨✨")
    min_length = int(input("Please enter a longer magic length: "))

has_number = input("Shall we sprinkle some enchanting numbers in your magic word? (yes/no): ").lower() == "yes"
has_special = input("How about adding some mystical special characters? (yes/no): ").lower() == "yes"

print("Let the magic begin...🔮✨")

pwd = generate_password(min_length, has_number, has_special)

print("Abracadabra! Your mystical password is ready to unveil:", pwd)

print("Now let's evaluate the strength of your magic word! 🧙‍♂️✨")
strength = evaluate_password_strength(pwd)
print("🔒 Password Strength:", strength, "out of 6") # 6 indicates the maximum strength
print("The higher the score, the stronger your magic word is! 💪✨")


