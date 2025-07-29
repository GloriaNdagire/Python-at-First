# QUESTION THREE
import sys
print("Hello and Welcome to this page, thank you for visiting us and we hope to give you a nice experience!!!")

contacts = {'glosh'  : '0700000000', 
            'gloria' : '0777777777', 
            'daddy'  : '0788888888',
            'benja'  : '0788888888',
            'lydia'  : '0799999999',
            'ezekiel': '0800000000',
            'melanie': '0811111111'
          }

while True:
 print("___Menu___")
 print(" ")
 print("1. Add a new contact")
 print("2. View all Contacts")
 print("3. Search for a contact by name")
 print("4. Delete a contact")
 print("5. Exit the program")  

 try:
    choice = int(input("Choose by number what you want: ")) 
 except ValueError:
        print("Please enter a value among the options in the menu above.")
        
 if choice == 1:
     add = input("Add name of contact: ")
     if add not in contacts:
        contacts[add] = input('Add the phone number: ')
        print(contacts)
     else:
          print("This contact already exits!")   
 
 elif choice == 2:
        print(contacts) 

 elif choice == 3:
        one = str(input("Search by name: "))   
        if one in contacts:
            print(f"{one}: {contacts[one]}")   #I had used print(one), but the other is better than this because it prints both name and number
        elif one not in contacts:
             print("Go to Add a new contact")
        
 elif choice == 4:
       print(contacts)
       two = str(input("Search by name what you want to delete: "))
       if two in contacts:
            del contacts[two]
            print(f"Deleting {two} from contacts")
            print(contacts)
    
 elif choice == 5:
        print("Exiting program.................") 
        sys.exit()  




'''
## AN UPGRADED VERSION

import sys

print("Hello and Welcome to this page! Thank you for visiting us. We hope to give you a nice experience!\n")

# Contacts now use nested dictionaries to store phone & email
contacts = {
    'glosh': {'phone': '0700000000', 'email': 'glosh@email.com'},
    'gloria': {'phone': '0777777777', 'email': 'gloria@email.com'},
    'daddy': {'phone': '0788888888', 'email': 'daddy@email.com'},
    'benja': {'phone': '0788888888', 'email': ''},
    'lydia': {'phone': '0799999999', 'email': ''},
    'ezekiel': {'phone': '0800000000', 'email': ''},
    'melanie': {'phone': '0811111111', 'email': ''}
}

while True:
    print("\n___Menu___")
    print("1. Add or Update a contact")
    print("2. View all Contacts")
    print("3. Search for a contact by name")
    print("4. Delete a contact")
    print("5. Exit the program")

    try:
        choice = int(input("\nChoose by number what you want: "))
    except ValueError:
        print("❌ Please enter a valid number from the menu.")
        continue

    # 1. Add or Update
    if choice == 1:
        name = input("Enter contact name: ").lower()
        phone = input("Enter phone number: ")
        email = input("Enter email (optional): ")

        if name in contacts:
            print(f"✅ Contact '{name}' exists. Updating info...")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"✅ Contact saved: {name} -> {contacts[name]}")

    # 2. View all
    elif choice == 2:
        if not contacts:
            print("📭 No contacts available.")
        else:
            print("\n📒 All Contacts:")
            for name, info in contacts.items():
                print(f"{name.title()}: Phone - {info['phone']}, Email - {info['email']}")

    # 3. Search
    elif choice == 3:
        search = input("Enter name to search: ").lower()
        if search in contacts:
            info = contacts[search]
            print(f"🔍 Found: {search.title()} -> Phone: {info['phone']}, Email: {info['email']}")
        else:
            print("❌ Contact not found. Try adding it first.")

    # 4. Delete
    elif choice == 4:
        delete = input("Enter name to delete: ").lower()
        if delete in contacts:
            del contacts[delete]
            print(f"🗑️ Deleted contact '{delete}'.")
        else:
            print("❌ Contact not found.")

    # 5. Exit
    elif choice == 5:
        print("👋 Exiting program... Goodbye!")
        sys.exit()

    else:
        print("❌ Invalid choice. Try again.")

'''                       
         
                  

