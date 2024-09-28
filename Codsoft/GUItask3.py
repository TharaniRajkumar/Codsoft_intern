import tkinter as tk
import random
import string
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        
        
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=10)
        
        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.pack(pady=5)
        
        
        self.include_upper = tk.IntVar()
        self.include_lower = tk.IntVar()
        self.include_digits = tk.IntVar()
        self.include_special = tk.IntVar()
        
        self.upper_check = tk.Checkbutton(root, text="Include Uppercase", variable=self.include_upper)
        self.upper_check.pack(anchor='w', padx=20)
        
        self.lower_check = tk.Checkbutton(root, text="Include Lowercase", variable=self.include_lower)
        self.lower_check.pack(anchor='w', padx=20)
        
        self.digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.include_digits)
        self.digits_check.pack(anchor='w', padx=20)
        
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special)
        self.special_check.pack(anchor='w', padx=20)
        
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        
        self.result_label = tk.Label(root, text="Generated Password:")
        self.result_label.pack(pady=10)
        
        self.password_display = tk.Entry(root, width=40, state='readonly')
        self.password_display.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
            
            char_pool = ""
            
            if self.include_upper.get():
                char_pool += string.ascii_uppercase
            if self.include_lower.get():
                char_pool += string.ascii_lowercase
            if self.include_digits.get():
                char_pool += string.digits
            if self.include_special.get():
                char_pool += string.punctuation
            
            if not char_pool:
                messagebox.showwarning("Selection Error", "Please select at least one character type.")
                return

            
            password = ''.join(random.choice(char_pool) for _ in range(length))
            
            
            self.password_display.config(state='normal')
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the length.")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
