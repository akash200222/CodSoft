import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate():
    password = generate_password(int(entry_length.get()))
    return_label.config(text="Generated Password: " + password)

def reset():
    return_label.config(text="")
    entry_length.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Label and entry for password length
label_length= ttk.Label(root, text="Password Length:")
label_length.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_length = ttk.Entry(root)
entry_length.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
entry_length.insert(tk.END,"")

# Button to generate password
button_generate = ttk.Button(root, text="Generate Password", command=generate)
button_generate.grid(row=1, column=0, pady=10)

# Button to reset
button_reset = ttk.Button(root, text="Reset", command=reset)
button_reset.grid(row=1, column=1, pady=10)

# Label to display generated password
return_label = ttk.Label(root, text="")
return_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
