def add_contact(contact_list):
    name = input("Enter contact name: ").strip()
    number = input("Enter contact number: ").strip()
    email = input("Enter contact email address: ").strip()
    

    contact_list[name] = {"Number": number, "Email": email}
    print(f"\nContact '{name}' added successfully!\n")


def display_contacts(contact_list):
    print("\n--- Contact List ---")
    if not contact_list:
        print("No contacts found.")
    else:
        for name, details in contact_list.items():
            print(f"Name: {name}")
            print(f"Number: {details['Number']}")
            print(f"Email: {details['Email']}\n")


def search_contact(contact_list):
    search_name = input("Enter the name of the contact to search: ").strip()
    if search_name in contact_list:
        print("\n--- Contact Found ---")
        print(f"Name: {search_name}")
        print(f"Number: {contact_list[search_name]['Number']}")
        print(f"Email: {contact_list[search_name]['Email']}\n")
    else:
        print("\nContact not found.\n")


def edit_contact(contact_list):
    name_to_edit = input("Enter the name of the contact to edit: ").strip()
    if name_to_edit in contact_list:
        print("\n--- Edit Contact ---")
        new_number = input("Enter new contact number: ").strip()
        new_email = input("Enter new contact email address: ").strip()
        
        
        contact_list[name_to_edit] = {"Number": new_number, "Email": new_email}
        print(f"\nContact '{name_to_edit}' updated successfully!\n")
    else:
        print("\nContact not found.\n")


def remove_contact(contact_list):
    name_to_remove = input("Enter the name of the contact to remove: ").strip()
    if name_to_remove in contact_list:
        del contact_list[name_to_remove]
        print(f"\nContact '{name_to_remove}' removed successfully!\n")
    else:
        print("\nContact not found.\n")


def manage_contacts():
    contact_list = {} 
    
    while True:
        print("\n--- Contact List Menu ---")
        print("A. Add a new contact")
        print("B. Display all contacts")
        print("C. Search for a contact")
        print("D. Edit a contact")
        print("E. Remove a contact")
        print("F. Exit the program")
        
        choice = input("Choose an option: ").strip().upper()
        
        if choice == "A":
            add_contact(contact_list)
        elif choice == "B":
            display_contacts(contact_list)
        elif choice == "C":
            search_contact(contact_list)
        elif choice == "D":
            edit_contact(contact_list)
        elif choice == "E":
            remove_contact(contact_list)
        elif choice == "F":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


manage_contacts()