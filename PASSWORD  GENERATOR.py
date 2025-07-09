import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate password
def generate_password():
    length_str = length_entry.get().strip()

    if not length_str:
        messagebox.showerror("Missing Input", "Please enter the password length.")
        return

    try:
        length = int(length_str)
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number.")
        return

    if length < 4:
        messagebox.showwarning("Too Short", "Password length should be at least 4 characters.")
        return

    character_pool = ""

    if var_upper.get():
        character_pool += string.ascii_uppercase
    if var_lower.get():
        character_pool += string.ascii_lowercase
    if var_digits.get():
        character_pool += string.digits
    if var_special.get():
        character_pool += string.punctuation

    if not character_pool:
        messagebox.showwarning("No Options Selected", "Please select at least one character type.")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# ---------------- GUI Setup ---------------- #
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Length input
frame_top = tk.Frame(root)
frame_top.pack(pady=5)
tk.Label(frame_top, text="Password Length:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(frame_top, width=5, font=("Helvetica", 12))
length_entry.grid(row=0, column=1, padx=5)

# Character type checkboxes
frame_check = tk.Frame(root)
frame_check.pack(pady=10)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(frame_check, text="Include Uppercase", variable=var_upper, font=("Helvetica", 11)).grid(sticky="w", padx=20)
tk.Checkbutton(frame_check, text="Include Lowercase", variable=var_lower, font=("Helvetica", 11)).grid(sticky="w", padx=20)
tk.Checkbutton(frame_check, text="Include Numbers", variable=var_digits, font=("Helvetica", 11)).grid(sticky="w", padx=20)
tk.Checkbutton(frame_check, text="Include Special Characters", variable=var_special, font=("Helvetica", 11)).grid(sticky="w", padx=20)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12), bg="#4CAF50", fg="white").pack(pady=10)

# Password display
password_entry = tk.Entry(root, font=("Helvetica", 14), width=30, justify="center")
password_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_password, font=("Helvetica", 12), bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()
