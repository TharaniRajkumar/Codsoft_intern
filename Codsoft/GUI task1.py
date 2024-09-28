import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")
        
        
        self.tasks = []
        
        
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_as_done)
        self.done_button.pack(pady=5)
        
        
        self.task_listbox = tk.Listbox(root, height=10, width=40)
        self.task_listbox.pack(pady=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
    
    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index] = updated_task
                self.update_task_listbox()
            else:
                messagebox.showwarning("Input Error", "Please enter an updated task.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
    
    def mark_as_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index] += " - Done"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
