import sqlite3
import tkinter as tk
from tkinter import messagebox

def create_table():
    connection = sqlite3.connect('letter.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            bio TEXT NOT NULL,
            health_directive TEXT,
            power_of_attorney TEXT,
            care_for_children TEXT,
            care_for_others TEXT,
            care_for_animals TEXT,
            contact_employer TEXT
        )''')

    connection.commit()
    connection.close()
    print("Table created successfully")

def update_table():
    connection = sqlite3.connect('letter.db')
    cursor = connection.cursor()

    cursor.execute("PRAGMA table_info(contacts)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'care_for_children' not in columns:
        cursor.execute('''ALTER TABLE contacts
                          ADD COLUMN care_for_children TEXT''')
    if 'care_for_others' not in columns:
        cursor.execute('''ALTER TABLE contacts
                          ADD COLUMN care_for_others TEXT''')
    if 'care_for_animals' not in columns:
        cursor.execute('''ALTER TABLE contacts
                          ADD COLUMN care_for_animals TEXT''')
    if 'contact_employer' not in columns:
        cursor.execute('''ALTER TABLE contacts
                          ADD COLUMN contact_employer TEXT''')

    connection.commit()
    connection.close()
    print("Table updated successfully")

def insert_contact(name, bio, health_directive, power_of_attorney, care_for_children, care_for_others, care_for_animals, contact_employer):
    connection = sqlite3.connect('letter.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO contacts (name, bio, health_directive, power_of_attorney, care_for_children, care_for_others, care_for_animals, contact_employer) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, bio, health_directive, power_of_attorney, care_for_children, care_for_others, care_for_animals, contact_employer))

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

def ask_health_directive():
    answer = messagebox.askquestion("Health Care Directives Applicable", "Review Health Care Directives Applicable: Yes or No")
    return answer

def ask_power_of_attorney():
    answer = messagebox.askquestion("Power of Attorney for Finances Applicable", "Review Power of Attorney for Finances Applicable: Yes or No")
    return answer

def ask_care_for_children():
    answer = messagebox.askquestion("Care for Children Applicable", "Care for Children Applicable: Yes or No")
    return answer

def ask_care_for_others():
    answer = messagebox.askquestion("Care for Others Applicable", "Care for Others Applicable: Yes or No")
    return answer

def ask_care_for_animals():
    answer = messagebox.askquestion("Care for Animals Applicable", "Care for Animals Applicable: Yes or No")
    return answer

def ask_contact_employer():
    answer = messagebox.askquestion("Contact Employer Applicable", "Contact Employer Applicable: Yes or No")
    return answer

def get_text():
    # Show the pop-up box
    messagebox.showinfo("WEEK 1", "Welcome to Week 1!")
    
    # Open the text entry window
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

def save_name(name, bio, name_window):
    health_directive = ask_health_directive()
    power_of_attorney = ask_power_of_attorney()
    care_for_children = ask_care_for_children()
    care_for_others = ask_care_for_others()
    care_for_animals = ask_care_for_animals()
    contact_employer = ask_contact_employer()
    
    insert_contact(name, bio, health_directive, power_of_attorney, care_for_children, care_for_others, care_for_animals, contact_employer)
    messagebox.showinfo('Success', 'Information saved successfully!')
    name_window.destroy()

# GUI setup
root = tk.Tk()
root.title('Contact Management')

# Create table if not exists
create_table()

# Update table structure if necessary
update_table()

# Button to enter text
text_button = tk.Button(root, text='Enter Text', command=get_text)
text_button.pack(pady=10)

# Button to print contacts
print_button = tk.Button(root, text='Print Contacts', command=print_contacts)
print_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()
