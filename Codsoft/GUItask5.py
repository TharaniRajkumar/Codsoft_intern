import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("500x500")
        
       
        self.contacts = {}
        
       
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack(pady=5)
        
        
        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.pack(pady=5)
        
       
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.pack(pady=5)
        
      
        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack(pady=5)
        self.address_entry = tk.Entry(root, width=30)
        self.address_entry.pack(pady=5)
        
      
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=10)
        
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=10)
        
        
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=10)
        
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=10)
        
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=10)
        
        
        self.contacts_listbox = tk.Listbox(root, height=10, width=50)
        self.contacts_listbox.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone and email and address:
            if name in self.contacts:
                messagebox.showwarning("Duplicate Entry", "Contact already exists.")
            else:
                self.contacts[name] = {
                    'phone': phone,
                    'email': email,
                    'address': address
                }
                messagebox.showinfo("Success", "Contact added successfully!")
                self.clear_entries()
        else:
            messagebox.showerror("Input Error", "All fields are required.")
    
    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name}: {details['phone']}")
    
    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            self.contacts_listbox.delete(0, tk.END)
            found = False
            for name, details in self.contacts.items():
                if search_term.lower() in name.lower() or search_term == details['phone']:
                    self.contacts_listbox.insert(tk.END, f"{name}: {details['phone']}")
                    found = True
            if not found:
                messagebox.showinfo("Not Found", "No contact found with that name or phone number.")
    
    def update_contact(self):
        selected = self.contacts_listbox.get(tk.ACTIVE)
        if selected:
            name = selected.split(":")[0].strip()
            if name in self.contacts:
                new_phone = simpledialog.askstring("Update Phone", "Enter new phone number:")
                new_email = simpledialog.askstring("Update Email", "Enter new email:")
                new_address = simpledialog.askstring("Update Address", "Enter new address:")
                
                if new_phone and new_email and new_address:
                    self.contacts[name]['phone'] = new_phone
                    self.contacts[name]['email'] = new_email
                    self.contacts[name]['address'] = new_address
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    self.view_contacts()
                else:
                    messagebox.showerror("Input Error", "All fields are required for updating.")
    
    def delete_contact(self):
        selected = self.contacts_listbox.get(tk.ACTIVE)
        if selected:
            name = selected.split(":")[0].strip()
            if name in self.contacts:
                confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {name}?")
                if confirm:
                    del self.contacts[name]
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    self.view_contacts()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
