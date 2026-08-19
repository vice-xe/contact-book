# -------- CONTACT BOOK -------- #

import json

# Save Contacts

def save_contacts():
    with open("contact.json","w") as file:
          json.dump(contacts, file)

# Load Contacts

def load_contacts():
    try:
        with open("contact.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


contacts = load_contacts()

while True:

    # Menu 

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit") 

    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("Please enter a number.")
        continue

    # Add Contacts

    if choice == 1:
        name = input("name:")
        phone = input("Phone:")
        email = input("Email:")

        contact = {
            "name":  name,
            "Phone": phone,
            "Email": email,
        }

        contacts.append(contact)
        save_contacts()

    # View Contact

    elif choice ==2:
        if not contacts:
            print("No contacts found.")
        else:
            for info in contacts:
                print("--- Contact ---")
                print("Name:",info["name"])
                print("Phone:",info["Phone"])
                print("Email:",info["Email"])

    # Search Contact 

    elif choice == 3:
        search = input("Search name:").strip().lower()
        found = False

        for info in contacts:
            if search == info["name"].strip().lower():
                print("--- Contact ---")
                print("Name:",info["name"])
                print("Phone:",info["Phone"])
                print("Email:",info["Email"])
                found = True

        if found == False:
            print("Name Does Not Found")

    # Delete Contact 

    elif choice ==4:
        delete = input("Search name:").strip().lower()
        found = False

        for info in contacts:
            if delete == info["name"].strip().lower():
                contacts.remove(info)
                save_contacts()
                found = True
                print("Contact deleted")
                break

        if found == False:
            print("Name Does Not Found")

    # Exit 

    elif choice ==5:
        print("Exiting...")
        break

    # Invalid Choice

    else:
        print("Invalid choice!") 
