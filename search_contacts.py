import csv
from load_contacts_from_file import load_contacts_from_file

def search_contacts_in_file(query):
    contacts = load_contacts_from_file()
    query = query.lower()


    results = [
        contact for contact in contacts
        if query in contact['name'].lower()
        or query in contact['email'].lower()
        or query in contact['phone_number']
        or query in contact['address'].lower()
    ]
    return results