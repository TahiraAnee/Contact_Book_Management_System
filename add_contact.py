from load_contacts_from_file import load_contacts_from_file
from save_contacts_to_file import save_all_contacts
contacts = []
contacts=load_contacts_from_file()
def add_contact(name, email, phone_number, address):
    # Prevent duplicate phone numbers
    for contact in contacts:
        if contact['phone_number'] == phone_number:
            print("Error: This phone number already exists.")
            return

    # Create new contact and append to contacts list
    contacts.append({
        'name': name,
        'email': email,
        'phone_number': phone_number,
        'address': address
    })
    print(f"Contact {name} added successfully.")
    save_all_contacts(contacts)