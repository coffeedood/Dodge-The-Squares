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
    # Close the main window
    root.destroy()
    
    # Open the text entry window
    text_window = tk.Tk()
    text_window.attributes('-fullscreen', True)  # Set to full screen
    text_window.title('Write a short summary of important biographical information.')
    tk.Label(text_window, text='Biography:', font=('Arial', 16)).grid(row=0, column=0, padx=20, pady=20)
    text_entry = tk.Text(text_window, height=10, width=50, font=('Arial', 14))  # Increased size of the text box
    text_entry.grid(row=1, column=0, padx=20, pady=20)
    
    submit_button = tk.Button(text_window, text='Submit', command=lambda: save_text(text_entry, text_window))
    submit_button.grid(row=2, column=0, padx=20, pady=20)
    
    # Bring the text entry window to the front and focus it
    text_window.grab_set()
    text_entry.focus_force()
    
    text_window.mainloop()

def save_text(text_entry, text_window):
    text = text_entry.get("1.0", "end-1c").strip()
    text_window.destroy()

    open_enter_name_window(text)

def open_enter_name_window(bio):
    name_window = tk.Tk()
    name_window.attributes('-fullscreen', True)  # Set to full screen
    name_window.title('Enter Name')
    
    tk.Label(name_window, text='Enter Name:', font=('Arial', 16)).grid(row=0, column=0, padx=20, pady=20)
    name_entry = tk.Entry(name_window, font=('Arial', 14))
    name_entry.grid(row=0, column=1, padx=20, pady=20)
    
    submit_button = tk.Button(name_window, text='Submit', command=lambda: save_name(name_entry.get(), bio, name_window))
    submit_button.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    
    # Bring the name entry window to the front and focus it
    name_window.grab_set()
    name_entry.focus_force()
    
    name_window.mainloop()

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
root.attributes('-fullscreen', True)  # Set to full screen
root.title('Contact Management')

# Create table if not exists
create_table()

# Update table structure if necessary
update_table()

# Button to enter text
text_button = tk.Button(root, text='Start', command=get_text, font=('Arial', 16))
text_button.pack(pady=10)

# Button to print contacts
print_button = tk.Button(root, text='Print Contacts', command=print_contacts, font=('Arial', 16))
print_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()
