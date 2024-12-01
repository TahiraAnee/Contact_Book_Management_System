import csv
from view_all_contacts import view_all_contacts
def update_contact_list():
    l = []
    new_phone_number = input("Enter a new phone number for update the contact list: ")
    found = False

    with open('Contact_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == new_phone_number:
                found = True
                print(f"Current Data: {row}")
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                row[0] = new_name
                row[1] = new_email
                row[3] = new_address
            l.append(row)

    if not found:
        print("Book not found.\n")
    else:

        with open('Contact_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(l)
        print("Contact updated successfully!")

        view_all_contacts()