import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x300")
        
        
        self.num1_entry = tk.Entry(root, width=20)
        self.num1_entry.pack(pady=10)
        self.num1_entry.insert(0, "Enter first number")
        
        self.num2_entry = tk.Entry(root, width=20)
        self.num2_entry.pack(pady=10)
        self.num2_entry.insert(0, "Enter second number")
        
        
        self.add_button = tk.Button(root, text="Add", command=self.add)
        self.add_button.pack(pady=5)
        
        self.subtract_button = tk.Button(root, text="Subtract", command=self.subtract)
        self.subtract_button.pack(pady=5)
        
        self.multiply_button = tk.Button(root, text="Multiply", command=self.multiply)
        self.multiply_button.pack(pady=5)
        
        self.divide_button = tk.Button(root, text="Divide", command=self.divide)
        self.divide_button.pack(pady=5)
        
        
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.pack(pady=20)
        
    
    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None
    
    
    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.result_label.config(text=f"Result: {result}")
    
    
    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.result_label.config(text=f"Result: {result}")
    
    
    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.result_label.config(text=f"Result: {result}")
    
    
    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
            else:
                result = num1 / num2
                self.result_label.config(text=f"Result: {result}")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
