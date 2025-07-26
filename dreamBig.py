import sys

message = 'Hey cool new person i just met, howdy!, May i get the previlige to know an angel\'s name?'
print(message) 

myName = input()
print(" ")
message = 'How old are you?'
print (message)
myAge = input()

print("Wow!!!!!! so your name is {} and you are {} years old.!!" .format(myName, myAge))

print(" ")

print("For the following, answer Yes(1) or No(0)")

print(" ")

questions = [
    "Do you like ice cream?",
    "Did you Pray?",
    "Did you eat this morning?",
    "Do you enjoy playing violin?"
]

for question in questions:
    answer = input(question + " (1 / 0): ")
    if answer == "1":
        print("That's great!")
    elif answer == "0":
        print("Oh, that's too bad.")
    else:
        print("Please answer with 1 for Yes or 0 for No.")

print(" ")
print("....Menu....")        
print("1.View your name")        
print("2.Play Magic 8-ball")        
print("3.List of favorite animals")        
print("4.Exit program")        

print(" ")
def get_choice():
    try:
        choice = int(input("Choose by number what you want: "))
        return choice
    
        #return ("Choose by number what you want.")
        #choice = input()        
    except:
        print("Please enter a digit not a character!")

choice = get_choice()

if choice == 1:
    print("Your name is {}".format())
elif choice == 2:
    print("Magic 8-ball")
elif choice == 3:
    print("[Cat, Dog, Lion, Hyena, Kiwi]")
elif choice == 4:
    print("Exiting program....")  
    

print(" ")
animals = ['playing violin', 'chilling', 'getting something done', 'praying']
print("These are some of my favourite animals:")
for animal in animals:
    print(animal)

  
     
       
     



