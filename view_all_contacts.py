import csv

def view_all_contacts():
    try:
        with open("Contact_list.csv", 'r') as file:
            reader = csv.DictReader(file)  # Use DictReader to access rows as dictionaries
            print(f"|     Name      |     Email     |    Phone_Number     |     Address      |")
            print("-" * 70)
            for row in reader:
                print(f"{row['Name']} | {row['Email']} | {row['Phone_Number']} | {row['Address']}")
    except FileNotFoundError:
        print("Error: The file 'Contact_list.csv' does not exist.")
    except KeyError as e:
        print(f"Error: Missing column in the CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
