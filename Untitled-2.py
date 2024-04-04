import sqlite3
import tkinter as tk
from tkinter import messagebox

def create_table():
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS contacts''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            bio TEXT
        )
    ''')

    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_contact(name, phone, email, bio=None):
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO contacts (name, phone, email, bio) VALUES (?, ?, ?, ?)
    ''', (name, phone, email, bio))

    connection.commit()
    connection.close()

def retrieve_contacts():
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    connection.close()
    return contacts

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    bio = entry_bio.get("1.0", tk.END).strip()  # Get the biographical information from the text widget

    if name and phone and email:
        insert_contact(name, phone, email, bio)
        messagebox.showinfo('Success', 'Contact added successfully!')
        clear_entries()
    else:
        messagebox.showerror('Error', 'Please fill in all fields.')

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_bio.delete("1.0", tk.END)

def print_contacts():
    contacts = retrieve_contacts()
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print('No contacts available.')

# GUI setup
root = tk.Tk()
root.title('Contact Management')

# Create table if not exists
create_table()

# Labels and entry widgets for user input
tk.Label(root, text='Name:').grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text='Phone:').grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Label(root, text='Email:').grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

tk.Label(root, text='Biographical Information:').grid(row=3, column=0)
entry_bio = tk.Text(root, height=4, width=30)
entry_bio.grid(row=3, column=1)

# Buttons for add contact and print contacts
add_button = tk.Button(root, text='Add Contact', command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

print_button = tk.Button(root, text='Print Contacts', command=print_contacts)
print_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI main loop
root.mainloop()

#hey dude whats up
