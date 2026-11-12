import tkinter as tk
from tkinter import messagebox
import string
import secrets

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4 or length > 64:
            messagebox.showwarning("Warning", "Enter length between 4 and 64")
            return

        characters = ""

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Select at least one option")
            return

        password = "".join(secrets.choice(characters) for _ in range(length))
        password_var.set(password)

    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid length")

def copy_password():
    password = password_var.get()

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied successfully")
    else:
        messagebox.showwarning("Warning", "Generate a password first")

window = tk.Tk()
window.title("Password Generator")
window.geometry("500x550")
window.config(bg="#111827")
window.resizable(False, False)

password_var = tk.StringVar()

heading = tk.Label(
    window,
    text="PASSWORD GENERATOR",
    font=("Arial", 22, "bold"),
    bg="#111827",
    fg="white"
)
heading.pack(pady=25)

length_label = tk.Label(
    window,
    text="Password Length",
    font=("Arial", 13),
    bg="#111827",
    fg="white"
)
length_label.pack()

length_entry = tk.Entry(
    window,
    font=("Arial", 14),
    justify="center",
    width=15
)
length_entry.insert(0, "12")
length_entry.pack(pady=10)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

options_frame = tk.Frame(window, bg="#111827")
options_frame.pack(pady=15)

for text, variable in [
    ("Uppercase Letters (A-Z)", uppercase_var),
    ("Lowercase Letters (a-z)", lowercase_var),
    ("Numbers (0-9)", numbers_var),
    ("Special Characters (!@#)", symbols_var)
]:
    tk.Checkbutton(
        options_frame,
        text=text,
        variable=variable,
        font=("Arial", 11),
        bg="#111827",
        fg="white",
        selectcolor="#374151",
        activebackground="#111827",
        activeforeground="white"
    ).pack(anchor="w", pady=5)

generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 13, "bold"),
    bg="#2563eb",
    fg="white",
    width=22,
    cursor="hand2"
)
generate_button.pack(pady=15)

password_entry = tk.Entry(
    window,
    textvariable=password_var,
    font=("Arial", 14),
    justify="center",
    width=30,
    state="readonly"
)
password_entry.pack(pady=10)

copy_button = tk.Button(
    window,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 12, "bold"),
    bg="#059669",
    fg="white",
    width=22,
    cursor="hand2"
)
copy_button.pack(pady=10)

window.mainloop()