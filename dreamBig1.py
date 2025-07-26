#QUESTION TWO 
import datetime
import random
import sys

print("Hey there!!", end=" ")
print("Happy to you use vist this site")
print(" ")

print("What is your name ", end=" ")
myName = input()
print(" ")
print("How old are you?", end=" ")
myAge = input()
print(" ")

print(f"{myName} is {myAge} years old")
print(" ")

print("           ___Menu___")
print(" ")
print("1.Tell the current time.")
print("2.Random motivational quote.")
print("3.Add items to a grocery list.")
print("4.View grocery list.")
print("5. Exit the program.")

def get_choice():
    choice = int(input("Enter by number, what you want to go into: "))
    if choice == 1:
        now = datetime.datetime.now()
        print("The time is:", now.strftime("%H:%M:%S"))
        #you can aslo do this print("The time is:", datetime.datetime.now().strftime("%H:%M:%S"))
    elif choice == 2: 
        quotes = [
                  'Always be confident in yourself and the tools you have',
                  'The top of one mountain is the bottom of the next, so keep climbing',
                  'Always know you are so blessed',
                  'Ask for extra ordinary favour from God'
                  ] 
        g = random.choice(quotes)   #r = random.randint(quotes[0]:quotes[3])
        print(g)

    elif choice == 3:
        list = ['tomatoes', 'onion', 'watermelon', 'cabbage', 'carrot']
        #list = list.add(input("Add an item to the grocery list: ")) so here i used .add, but .add is for sets, and .append is for lists
        list.append(input("Add an item to the grocery list: "))
        print(list)
       
    elif choice == 4:
        list = ['tomatoes', 'onion', 'watermelon', 'cabbage', 'carrot']
        print(list)
    elif choice == 5:
        print("Exiting program.................") 
        sys.exit() 
    else:
        print("Invalid option try again.")      


get_choice()



# MORE DEVELOPED CODE
'''
import datetime
import random
import sys

print("Hey there!! Happy to have you visit this site\n")

myName = input("What is your name? ")
myAge = input("How old are you? ")

print(f"\n{myName} is {myAge} years old\n")

# Persistent grocery list
grocery_list = ['tomatoes', 'onion', 'watermelon', 'cabbage', 'carrot']

while True:
    print("\n           ___Menu___\n")
    print("1. Tell the current time.")
    print("2. Random motivational quote.")
    print("3. Add items to a grocery list.")
    print("4. View grocery list.")
    print("5. Exit the program.")

    try:
        choice = int(input("\nEnter by number what you want to go into: "))
    except:
        print("❌ Please enter a valid number!")
        continue

    if choice == 1:
        now = datetime.datetime.now()
        print("The time is:", now.strftime("%H:%M:%S"))

    elif choice == 2: 
        quotes = [
            'Always be confident in yourself and the tools you have',
            'The top of one mountain is the bottom of the next, so keep climbing',
            'Always know you are so blessed',
            'Ask for extraordinary favour from God'
        ] 
        print(random.choice(quotes))
        
    elif choice == 3:
        item = input("Add an item to the grocery list: ")
        grocery_list.append(item)
        print("Item added! Current list:", grocery_list)

    elif choice == 4:
        print("Your grocery list:", grocery_list)

    elif choice == 5:
        print("Exiting program.................")
        sys.exit()

    else:
        print("❌ Invalid option, try again.")

'''

