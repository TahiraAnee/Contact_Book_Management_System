
def validate_contact_input(name,email,phone_number,address):
    errors = []

    if not name.isalpha() and not None :
        errors.append("The contact's name must contain only alphabetic characters.")


    if not phone_number.isdigit() and not None:
        errors.append("The phone number must be a numeric value.")

    if "@" not in email or "." not in email.split("@")[-1] and not None:
        errors.append("The email address is invalid. Ensure it contains '@' and a domain name.")

    if not address and not None:
        errors.append("The address field cannot be empty.")

    if errors:
        print("Invalid input detected:")
        for error in errors:
            print(f"- {error}")
        print("Please try again with correct inputs.\n")
        return False

    return True
