import re

COMMON_PASSWORDS = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein"
]

def main():
    password = input("Enter your password: ")
    strength = evaluate_password(password)
    print(f"Password Strength: {strength}")


def evaluate_password(password):
    if is_common_password(password):
        return "Very Weak"

    score = 0

    if len(password) >= 8:
        score += 1
    if has_uppercase(password):
        score += 1
    if has_lowercase(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_special_char(password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_special_char(password):
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))


def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS


if __name__ == "__main__":
    main()

