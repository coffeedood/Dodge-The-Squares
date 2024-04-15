import sqlite3
import tkinter as tk
from tkinter import messagebox

def create_table():
    connection = sqlite3.connect('letter.db')
    cursor = connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS contacts''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            bio TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_contact(name, bio):
    connection = sqlite3.connect('letter.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO contacts (name, bio) VALUES (?, ?)
    ''', (name, bio))

    connection.commit()
    connection.close()

def retrieve_contacts():
    connection = sqlite3.connect('letter.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    connection.close()
    return contacts

def print_contacts():
    contacts = retrieve_contacts()
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print('No contacts available.')

def get_text():
    text_window = tk.Toplevel(root)
    text_window.title('Enter Text')
    
    tk.Label(text_window, text='Enter Text:').grid(row=0, column=0)
    text_entry = tk.Text(text_window, height=4, width=30)
    text_entry.grid(row=0, column=1)
    
    submit_button = tk.Button(text_window, text='Submit', command=lambda: save_text(text_entry))
    submit_button.grid(row=1, column=0, columnspan=2, pady=10)

def save_text(text_entry):
    text = text_entry.get("1.0", "end-1c").strip()
    name_window = tk.Toplevel(root)
    name_window.title('Enter Name')
    
    tk.Label(name_window, text='Enter Name:').grid(row=0, column=0)
    name_entry = tk.Entry(name_window)
    name_entry.grid(row=0, column=1)
    
    submit_button = tk.Button(name_window, text='Submit', command=lambda: save_name(name_entry.get(), text, name_window))
    submit_button.grid(row=1, column=0, columnspan=2, pady=10)

def save_name(name, text, name_window):
    insert_contact(name, text)
    messagebox.showinfo('Success', 'Text saved successfully!')
    name_window.destroy()

# GUI setup
root = tk.Tk()
root.title('Contact Management')

# Create table if not exists
create_table()

# Button to enter text
text_button = tk.Button(root, text='Enter Text', command=get_text)
text_button.pack(pady=10)

# Button to print contacts
print_button = tk.Button(root, text='Print Contacts', command=print_contacts)
print_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()
