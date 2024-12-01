import csv
def save_all_contacts(contacts):
    with open("Contact_list.csv",mode='w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone_Number", "Address"])
        for data in contacts:
            writer.writerow([data['name'],data['email'],data['phone_number'],data['address']])

