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
 
 elif choice == 2:
        print(contacts) 

 elif choice == 3:
        one = str(input("Search by name: "))
        if one in contacts:
            print(one)
        elif one not in contacts:
             print("Go to Add a new contact")
        break
 elif choice == 4:
       print(contacts)
       two = str(input("Search by name what you want to delete: "))
       if two in contacts:
            del contacts[two]
            print(f"Deleting {two} from contacts")
            print(contacts)
       break 
 elif choice == 5:
        print("Exiting program.................") 
        sys.exit()    
                       
         
                  

