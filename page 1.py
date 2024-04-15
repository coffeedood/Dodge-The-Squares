import sqlite3
import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Contact and Task Management')

        # Initialize checkbox variables
        self.care_for_children_var = tk.BooleanVar()
        self.care_for_others_var = tk.BooleanVar()
        self.care_for_animals_var = tk.BooleanVar()
        self.contact_employer_var = tk.BooleanVar()

        self.create_contact_table()
        self.create_task_table()

        self.setup_gui()

        self.root.mainloop()

    def create_contact_table(self):
        connection = sqlite3.connect('contacts.db')
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
        print("Contact table created successfully")

    def create_task_table(self):
        connection = sqlite3.connect('tasks.db')
        cursor = connection.cursor()

        cursor.execute('''DROP TABLE IF EXISTS tasks''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                care_for_children TEXT NOT NULL,
                care_for_others TEXT NOT NULL,
                care_for_animals TEXT NOT NULL,
                contact_employer TEXT NOT NULL
            )
        ''')

        connection.commit()
        connection.close()
        print("Task table created successfully")

    def insert_contact(self, name, bio):
        connection = sqlite3.connect('contacts.db')
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO contacts (name, bio) VALUES (?, ?)
        ''', (name, bio))

        connection.commit()
        connection.close()

    def insert_tasks(self, care_for_children, care_for_others, care_for_animals, contact_employer):
        connection = sqlite3.connect('tasks.db')
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO tasks (care_for_children, care_for_others, care_for_animals, contact_employer)
            VALUES (?, ?, ?, ?)
        ''', (care_for_children, care_for_others, care_for_animals, contact_employer))

        connection.commit()
        connection.close()

    def setup_gui(self):
        tk.Label(self.root, text='Enter Name:').pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text='Enter Bio:').pack()
        self.bio_entry = tk.Text(self.root, height=4, width=30)
        self.bio_entry.pack()

        tk.Checkbutton(self.root, text='Care for Children', variable=self.care_for_children_var).pack()
        tk.Checkbutton(self.root, text='Care for Others', variable=self.care_for_others_var).pack()
        tk.Checkbutton(self.root, text='Care for Animals', variable=self.care_for_animals_var).pack()
        tk.Checkbutton(self.root, text='Contact Employer', variable=self.contact_employer_var).pack()

        tk.Button(self.root, text='Save', command=self.save_data).pack(pady=10)
        tk.Button(self.root, text='Print', command=self.print_data).pack(pady=10)

    def save_data(self):
        name = self.name_entry.get()
        bio = self.bio_entry.get("1.0", "end-1c").strip()

        self.insert_contact(name, bio)
        self.insert_tasks(self.care_for_children_var.get(), self.care_for_others_var.get(),
                          self.care_for_animals_var.get(), self.contact_employer_var.get())
        messagebox.showinfo('Success', 'Contact and Tasks saved successfully!')

    def print_data(self):
        connection = sqlite3.connect('contacts.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM contacts')
        contacts = cursor.fetchall()

        connection.close()

        if contacts:
            print("Contacts:")
            for contact in contacts:
                print(contact)
        else:
            print('No contacts available.')

        connection = sqlite3.connect('tasks.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()

        connection.close()

        if tasks:
            print("Tasks:")
            for task in tasks:
                print(task)
        else:
            print('No tasks available.')

ContactManager()
