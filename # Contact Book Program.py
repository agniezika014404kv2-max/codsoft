# Contact Book Program

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
    else:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
        print()

def search_contact():
    search = input("Enter Name or Phone to search: ")
    found = False
    for name, details in contacts.items():
        if name == search or details['phone'] == search:
            print(f"\nContact Found:\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new Phone Number: ")
        email = input("Enter new Email: ")
        address = input("Enter new Address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact {name} updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
