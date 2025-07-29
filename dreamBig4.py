#QUESTION FIVE, TO-DO LIST APP
import sys
import json
import os

'''
if os.path.exists("tasks.json"):
    print("File exists")
else:
    print("File does not exist")    
'''
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as f:
        todoList = json.load(f) #load dictionary from file
else:
    todoList = {}


def save_data():
    with open("tasks.json", "w") as f:
        json.dump(todoList, f)

while True:        
 print("Welcome to your To-Do List App!")
 print(" ")
 print("___MENU___")
 print(" ")
 print("1. Add a new task")
 print("2. View all tasks")
 print("3. Mark a task as done")
 print("4. Delete a task")
 print("5. Exit the program")
 try:
     choice = int(input("Choose by number what you want: "))    
 except ValueError:
    print("❌ Please enter a valid number from the menu.")  
    continue

 if choice == 1:
    task = input("Enter the task you want to add: " )
    if task not in todoList:
        todoList[task] = False
        save_data()
    else:
        print("This task already exists in your To-Do List.")

 elif choice == 2:
     print(todoList)

 elif choice == 3:
    task = input("Enter the task you want to mark as done: " )
    if task in todoList:  
        todoList[task] = True
        save_data()
    else:
        print("This task does not exist in your To-Do List.")                  
        print("Please go to option 1 to add it.")        

 elif choice == 4:     
     task = input("✔️Enter the task you want to delete: " )  
     del todoList[task]
     save_data()           
     print(f"Deleted {task} from your To-Do List.")

 elif choice == 5:
     print("Exiting program.................") 
     sys.exit()      


     