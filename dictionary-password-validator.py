import numpy as np
import tkinter as tk
from tkinter import messagebox

# --- Core Security Logic Function ---
def check_password_strength():
    # Retrieve what the user typed into the GUI box
    user_password = password_entry.get()
    
    # 1. Load the Common Passwords list
    try:
        with open("common_passwords.txt", "r") as file:
            common_list = [line.strip() for line in file.readlines()]
        banned_passwords = np.array(common_list)
    except FileNotFoundError:
        banned_passwords = np.array(["123456", "password", "qwerty", "admin123"])

    # 2. Check against the common password array
    is_common = False
    for weak_pass in banned_passwords:
        if user_password == weak_pass:
            is_common = True
            break

    if is_common:
        messagebox.showerror("Security Verdict", "❌ Kindly think before creating password:\nCommon words/patterns are used in this password!")
        return

    # 3. Check for Complexity Rules
    password_array = np.array(list(user_password))
    has_digit = False
    has_special = False
    special_characters = np.array(['!', '@', '#', '$', '%', '^', '&', '*'])

    for char in password_array:
        if char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # 4. Display Results in a Graphical Pop-up Window
    if len(password_array) >= 8 and has_digit and has_special:
        messagebox.showinfo("Security Verdict", "✅ Strong Password:\nMeets all security policies!")
    else:
        messagebox.showwarning("Security Verdict", "❌ Weak Password:\nMust be 8+ characters, include a number and a special character.")


# --- Window UI Setup ---
# Initialize the main window
root = tk.Tk()
root.title("Cyber Security Password Validator")
root.geometry("1400x800")
root.configure(bg="#2c3e50") # Dark slate background for a security tool look

# Instruction Label
instruction_label = tk.Label(root, text="Enter a Secure Password to Validate:", font=("Arial", 70, "bold"), fg="#ecf0f1", bg="#2c3e50")
instruction_label.pack(pady=15)

# Password Input Field (show="*" hides the typing for shoulder-surfing safety)
password_entry = tk.Entry(root, font=("Arial", 70), width=25, show="*")
password_entry.pack(pady=5)

# Validate Button
# When clicked, command=check_password_strength fires off our NumPy function above
validate_button = tk.Button(root, text="Scan Password", font=("Arial", 70, "bold"), fg="#062d17", bg="white", width=15, command=check_password_strength)
validate_button.pack(pady=20)

# Keep the window running on the desktop screen
root.mainloop()