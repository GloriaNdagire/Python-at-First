# QUESTION THREE
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
 print("1.1. Add a contact")
 print("1.2. View all Contacts")
 print("1.3. Search for a contact by name")
 print("1.1. Delete a contact")
 print("1.5. Exit the program")  

 try:
    choice = int(input("Choose by number what you want: ")) 
 except ValueError:
        print("Please enter a value among the options in the menu above.")

 if choice == 1:
     add = input("Add name of contact: ")
     if add not in contacts:
         contacts[add] = int(input("Add the phone number: ))
         print(contacts)

