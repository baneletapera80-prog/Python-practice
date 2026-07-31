contact = []

def add_contact(name, phone, email, address):
    contact_info = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contact.append(contact_info)

def view_contacts():
    if not contact:
        print("No contacts in the contact book.")
        return
    for index, person in enumerate(contact, start=1):
        print(f"{index}. Name: {person['name']}, Phone: {person['phone']}, Email: {person['email']}, address: {person['address']}")

def search_contact(query):  
    found_contacts = [person for person in contact if query.lower() in person['name'].lower() or query.lower() in person['phone'].lower()]
    if not found_contacts:
        print("No matching contacts found.")
        return
    print("\nSearch Results:")
    for index, person in enumerate(found_contacts, start=1):
        print(f"{index}. Name: {person['name']}, Phone: {person['phone']}, Email: {person['email']}, address: {person['address']}")

def update_contact(index, name, phone, email,address):
    if index < 1 or index > len(contact):
        print("Invalid contact index.")
        return
    contact[index - 1] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact updated successfully.")

def delete_contact(index):
    if index < 1 or index > len(contact):
        print("Invalid contact index.")
        return
    contact.pop(index - 1)
    print("Contact deleted successfully.")

def call_contact(index):
    if index < 1 or index > len(contact):
        print("Invalid contact index.")
        return
    person = contact[index - 1]
    print(f"Calling {person['name']} at {person['phone']}...")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Call Contact")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            add_contact(name, phone, email, address)
            print("Contact added successfully.")
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            query = input("Enter contact name or phone to search: ")
            search_contact(query)
        elif choice == '4':
            view_contacts()
            index = int(input("Enter the number of the contact to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            update_contact(index, name, phone, email, address)
        elif choice == '5':
            view_contacts()
            index = int(input("Enter the number of the contact to delete: "))
            delete_contact(index)
        elif choice == '6':
            view_contacts()
            index = int(input("Enter the number of the contact to call: "))
            call_contact(index)
        elif choice == '7':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()