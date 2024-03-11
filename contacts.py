import sys

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        print('Name\t\tPhone\t\tEmail\t\tAddress')
        for contact in self.contacts:
            print(f'{contact.name}\t{contact.phone}\t{contact.email}\t{contact.address}')

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword.lower() in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, name, new_contact):
        for contact in self.contacts:
            if contact.name == name:
                contact.name = new_contact.name
                contact.phone = new_contact.phone
                contact.email = new_contact.email
                contact.address = new_contact.address
                break

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                break

def main():
    contact_book = ContactBook()
    while True:
        print('\nContact Book')
        print('1. Add Contact')
        print('2. View Contact List')
        print('3. Search Contact')
        print('4. Update Contact')
        print('5. Delete Contact')
        print('6. Exit')
        option = input('Choose an option: ')
        if option == '1':
            name = input('Enter name: ')
            phone = input('Enter phone: ')
            email = input('Enter email: ')
            address = input('Enter address: ')
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif option == '2':
            contact_book.view_contacts()
        elif option == '3':
            keyword = input('Enter name or phone to search: ')
            results = contact_book.search_contact(keyword)
            if results:
                print('Search Results:')
                for contact in results:
                    print(f'{contact.name}\t{contact.phone}')
            else:
                print('No results found.')
        elif option == '4':
            name = input('Enter name of contact to update: ')
            new_name = input('Enter new name: ')
            new_phone = input('Enter new phone: ')
            new_email = input('Enter new email: ')
            new_address = input('Enter new address: ')
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_book.update_contact(name, new_contact)
        elif option == '5':
            name = input('Enter name of contact to delete: ')
            contact_book.delete_contact(name)
        elif option == '6':
            sys.exit(0)
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()
