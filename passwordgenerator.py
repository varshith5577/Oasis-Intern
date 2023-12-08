import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        
        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=8)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.specialchar_var = tk.BooleanVar(value=True)
        
        label = tk.Label(root, text="PASSWORD GENERATOR", font=("Helvetica", 20))
        label.pack(pady=10)
        length_label = tk.Label(root, text="Password Length", font=("Helvetica", 12))
        length_label.pack()
        length_entry = tk.Entry(root, textvariable=self.length_var)
        length_entry.pack()
        complexity_frame = ttk.LabelFrame(root, text="Password Complexity")
        complexity_frame.pack(pady=10)
        tk.Checkbutton(complexity_frame, text="Lowercase Letters", variable=self.lowercase_var, font=("Helvetica", 10)).pack(anchor=tk.W)
        tk.Checkbutton(complexity_frame, text="Uppercase Letters", variable=self.uppercase_var, font=("Helvetica", 10)).pack(anchor=tk.W)
        tk.Checkbutton(complexity_frame, text="Digits", variable=self.digits_var, font=("Helvetica", 10)).pack(anchor=tk.W)
        tk.Checkbutton(complexity_frame, text="Special Characters", variable=self.specialchar_var, font=("Helvetica", 10)).pack(anchor=tk.W)
        generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 11), command=self.generate_password)
        generate_button.pack(pady=10)
        password_label = tk.Label(root, text="Generated Password", font=("Helvetica", 10))
        password_label.pack()
        password_entry = tk.Entry(root, textvariable=self.password_var, state='readonly', font=("Helvetica", 10))
        password_entry.pack()
        copy_button = tk.Button(root, text="Copy", font=("Helvetica", 10), command=self.copy_to_clipboard)
        copy_button.pack(pady=20)
        
    def generate_password(self):
        password_characters = ""
        
        if self.lowercase_var.get():
            password_characters += string.ascii_lowercase
        if self.uppercase_var.get():
            password_characters += string.ascii_uppercase
        if self.digits_var.get():
            password_characters += string.digits
        if self.specialchar_var.get():
            password_characters += string.punctuation
        
        if not password_characters:
            messagebox.showinfo('','Select at least one character set')
        else:
            length = self.length_var.get()
            password = "".join(random.choice(password_characters) for _ in range(length))
            self.password_var.set(password)
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
