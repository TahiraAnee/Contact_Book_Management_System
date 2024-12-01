import add_contact
import update_contacts
from add_contact import add_contact
from validate_contact_input import validate_contact_input
from load_contacts_from_file import load_contacts_from_file
from view_all_contacts import view_all_contacts
from remove_contacts_from_file import remove_contacts_from_file
from search_contacts import search_contacts_in_file
from update_contacts import update_contact_list
def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Update Contact")
    print("6. Exit")



global contacts
contacts = load_contacts_from_file()

while True:
    display_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        phone_number = input("Enter Phone Number: ").strip()
        address = input("Enter Address: ").strip()

        if validate_contact_input(name, email, phone_number, address):
            add_contact(name, email, phone_number, address)

    elif choice == '2':
        view_all_contacts()
    elif choice == '3':
        phone_number = input("Enter phone number to remove: ")
        remove_contacts_from_file(phone_number)
    elif choice == '4':
        query = input("Enter Value to search: ")
        results = search_contacts_in_file(query)
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(
                    f" Name: {contact['name']},\n Email: {contact['email']},\n Phone: {contact['phone_number']},\n Address: {contact['address']}")
        else:
            print("No matching contacts found.")
    elif choice == '5':
        update_contacts.update_contact_list()
    elif choice == '6':
        print("Exiting the contact book system.")
        break
    else:
        print("Invalid choice. Please try again.")