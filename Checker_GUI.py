import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length
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

    # Evaluate
    if score <= 2:
        return "Weak", suggestions, "red"
    elif score <= 4:
        return "Moderate", suggestions, "orange"
    else:
        return "Strong", suggestions, "green"

# GUI
def evaluate_password():
    pwd = entry.get()
    strength, tips, color = check_password_strength(pwd)
    strength_label.config(text=f"Strength: {strength}", fg=color)

    # Clear previous suggestions
    suggestions_text.delete(1.0, tk.END)
    if tips:
        suggestions_text.insert(tk.END, "Suggestions:\n")
        for t in tips:
            suggestions_text.insert(tk.END, f"- {t}\n")

# Main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=10)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 14, "bold"))
strength_label.pack(pady=10)

suggestions_text = tk.Text(root, height=8, width=45, wrap="word")
suggestions_text.pack(pady=5)

root.mainloop()
