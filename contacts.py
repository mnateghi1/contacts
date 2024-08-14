# contacts.py
import json
import re


class Contacts:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        if not re.match(r'^[a-zA-Z\s]+$', name):
            print("Invalid name format. Contact didn't add.")
            return
        if not re.match(r'^09[0-9]{9}$', phone) or re.match(r'^\+989[0-9]{9}$', phone) or re.match(r'^00989[0-9]{9}$', phone):
            print("Invalid phone number format. Contact didn't add.")
            return
        if not re.match(r'^[a-z A-Z 0-9 \_ \.]+@[a-z A-Z 0-9]+\.[a-z A-Z]{3}$', email):
            print("Invalid email format. Contact didn't add.")
            return
        self.contacts.append({'name': name, 'phone': phone, 'email': email})
        self.save_contacts()
        print(f"✅ Contact '{name}' added successfully.")

    def edit_contact(self, old_name, new_name, new_phone, new_email):
        for contact in self.contacts:
            if contact['name'] == old_name:
                contact['name'] = new_name
                contact['phone'] = new_phone
                contact['email'] = new_email
                self.save_contacts()
                print(f"✅ Contact '{old_name}' edited successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]
        self.save_contacts()
        print(f"✅ Contact '{name}' removed successfully.")

    def display_contacts(self):
        print("Contacts:")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact['name'])
        self.save_contacts()
        print(f"✅ Contacts sorted successfully.")


con = Contacts()
print('<<<Contacts>>>')
while True:
    print('-' * 23,'Main Menu', '-' * 23)
    print('| 1️⃣  Add new contact                                   ', '|')
    print('| 2️⃣  Del contact                                       ', '|')
    print('| 3️⃣  Display contacts                                  ', '|')
    print('| 4️⃣  Edit contact                                      ', '|')
    print('| 5️⃣  Sort contacts                                     ', '|')
    print('| 0️⃣  Exit                                              ', '|')
    print('-' * 57)
    command = input('🔵 Please enter your command: ').strip()              
    while command not in ['0', '1', '2', '3', '4', '5']:
        print('-' * 57)
        command = input(f"⚠️  Command '{command}' is invalid!\n🔵 Please enter an option of 'Main Menu': ").strip()

    if command == '1':
        print('-' * 57)
        name = input('🔵 Please enter the name: ').strip()
        phone = input('🔵 Please enter the phone number: ').strip()
        email = input('🔵 Please enter the email address: ').strip()
        con.add_contact(name, phone, email)
            
    elif command == '2':
        print('-' * 57)
        name = input('🔵 Please enter the name: ').strip()
        con.delete_contact(name)

    elif command == '3':
        print('-' * 57)
        con.display_contacts()

    elif command == '4':
        print('-' * 57)
        old_name = input('🔵 Please enter the current name: ').strip()
        new_name = input('🔵 Please enter the new name: ').strip()
        new_phone = input('🔵 Please enter the new phone number: ').strip()
        new_email = input('🔵 Please enter the new email address: ').strip()
        con.edit_contact(old_name, new_name, new_phone, new_email)

    elif command == '5':
        print('-' * 57)
        con.sort_contacts()

    else: # for exit
        print('~' * 20, 'Have a good day', '~' * 20)
        break
