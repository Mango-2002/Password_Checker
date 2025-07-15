import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Digits
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include special characters.")

    # Common patterns
    weak_patterns = ["1234", "password", "qwerty"]
    if any(p in password.lower() for p in weak_patterns):
        score -= 1
        suggestions.append("Avoid common patterns like '1234' or 'password'.")

    # Strength evaluation
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions


# Run in console
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength, tips = check_password_strength(pwd)
    print(f"Password Strength: {strength}")
    if tips:
        print("Suggestions:")
        for t in tips:
            print("-", t)
