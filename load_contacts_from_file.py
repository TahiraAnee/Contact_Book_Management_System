import csv

def load_contacts_from_file():
    contact = []
    try:
        with open("Contact_list.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                contact.append({
                    'name': row[0],
                    'email': row[1],
                    'phone_number': row[2],
                    'address': row[3]
                })
    except FileNotFoundError:
        pass

    return contact

