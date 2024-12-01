import csv
from view_all_contacts import view_all_contacts
def remove_contacts_from_file(phone_number):
    l=[]
    found=False
    with open('Contact_list.csv','r',newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2]==phone_number:
                found=True
            else:
                l.append(row)
    if not found:
        print("Contact is not found.So we can't delete it.\n")
    else:
        with open('Contact_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(l)
            print("Contact Deleted successfully!")

        view_all_contacts()