import re
import tkinter as tk
from tkinter import messagebox

# Validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email)

# Process email
def process_email():
    email = entry_email.get().strip()

    if validate_email(email):
        username, domain = email.split("@")

        label_result.config(text="Valid Email", fg="green")
        label_username.config(text=f"Username: {username}")
        label_domain.config(text=f"Domain: {domain}")
    else:
        label_result.config(text="Invalid Email", fg="red")
        label_username.config(text="")
        label_domain.config(text="")

# Clear fields
def clear_fields():
    entry_email.delete(0, tk.END)
    label_result.config(text="")
    label_username.config(text="")
    label_domain.config(text="")

# GUI window
root = tk.Tk()
root.title("Email Processing System")
root.geometry("400x250")

# Widgets
tk.Label(root, text="Enter Email:", font=("Arial", 12)).pack(pady=10)

entry_email = tk.Entry(root, width=30, font=("Arial", 12))
entry_email.pack()

tk.Button(root, text="Process", command=process_email, width=15).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields, width=15).pack()

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=5)

label_username = tk.Label(root, text="", font=("Arial", 11))
label_username.pack()

label_domain = tk.Label(root, text="", font=("Arial", 11))
label_domain.pack()

root.mainloop()