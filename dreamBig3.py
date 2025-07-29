##QUESTION FOUR
import sys
message = ("Welcome to the Student Management System").upper()
print(message)

studentInfo = {
    'GLORIA': {'age' : '18', 'course': ['BCE', ' ']},
    'maria': {'age' : '17', 'course': ['BME']},
    'lydia': {'age' : '19', 'course': ['BEE']},
    'daddy': {'age' : '21', 'course': ['BSE']},
    'mummy': {'age' : '18', 'course': ['BCE']},
    'benja': {'age' : '19', 'course': ['BME']}
}

while True:
 print("___MENU___")
 print(" ")
 print("1.Add a new student.")
 print("2.View all students")
 print("3.Search for a student by name")
 print("4.Change a course of a student")
 print("5.Add a course to a student")
 print("6.Delete a student")

 try: 
        choose = int(input("Choose what you want to get into by number: "))
 except ValueError :
        print("Please choose any of the choices in the menu by number.") 

 if choose == 1:
    studentName = input("Enter Student name here: ")
    studentAge = input("Enter Student age here: ")
    studentCourse = input("Enter Student course here: ").upper()
    if studentName not in studentInfo:
        studentInfo[studentName] = {'age': studentAge, 'course': [studentCourse]}
        print(f"Added student: {studentName}, Age: {studentAge}, Course: {studentCourse}")
    else:
        print("This student already exists!")
    continue
 elif choose == 2:
        print(studentInfo)
        continue
 
 elif choose == 3:
    searchStudent = input("Enter name of student: ")
    one = studentInfo[searchStudent] 
    print(one)
    continue
 
 elif choose == 4: 
    searchStudent = input("Enter name of student: ")
    if searchStudent in studentInfo:
     changeCourse = input("Enter new course: ")
     former = studentInfo[searchStudent]['course']
     print("Former course:", former)
     studentInfo[searchStudent]['course'] = [changeCourse]
     print("Updated course:", studentInfo[searchStudent]['course'])
    else:
        print("This student does not exist!") 
    continue
 
 elif choose == 5:
    searchStudent = input("Enter name of student: ")
    if searchStudent in studentInfo:
        addCourse = input("Enter added course: ").upper()
        studentInfo[searchStudent]['course'].append(addCourse)
        print(f"{searchStudent} has now been enrolled in {studentInfo[searchStudent]['course']}")
    else:
        print("This student does not exist!")
    continue  
  
 elif choose == 6:
   searchStudent = input("Enter name of student: ")
   if searchStudent in studentInfo:
    del studentInfo[searchStudent]
    print(f"Deleted {searchStudent} from student records.")
   else:
    print("This student does not exist!")  


#BETTER VERSION
'''
import sys
import json
import os

FILE_NAME = "students.json"

# ✅ Load data from file if it exists
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        studentInfo = json.load(f)
else:
    studentInfo = {
        'gloria': {'age': '18', 'course': ['BCE']},
        'maria': {'age': '17', 'course': ['BME']},
        'lydia': {'age': '19', 'course': ['BEE']},
        'daddy': {'age': '21', 'course': ['BSE']},
        'mummy': {'age': '18', 'course': ['BCE']},
        'benja': {'age': '19', 'course': ['BME']}
    }

# ✅ Function to save data to file
def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump(studentInfo, f)

message = "Welcome to the Student Management System".upper()
print(message)

while True:
    print("\n___MENU___")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student by name")
    print("4. Change a course of a student")
    print("5. Add a course to a student")
    print("6. Delete a student")
    print("7. Exit program")

    try:
        choose = int(input("Choose what you want by number: "))
    except ValueError:
        print("⚠️ Please choose a valid number.")
        continue

    if choose == 1:
        studentName = input("Enter Student name: ").lower()
        studentAge = input("Enter Student age: ")
        studentCourse = input("Enter Student course: ").upper()

        if not studentName or not studentAge or not studentCourse:
            print("⚠️ All fields are required!")
            continue

        if studentName not in studentInfo:
            studentInfo[studentName] = {'age': studentAge, 'course': [studentCourse]}
            save_data()
            print(f"✅ Added student: {studentName.capitalize()} | Age: {studentAge} | Course: {studentCourse}")
        else:
            print("⚠️ This student already exists!")

    elif choose == 2:
        print("\n📌 All Students:")
        for name, info in studentInfo.items():
            print(f"{name.capitalize()} | Age: {info['age']} | Courses: {', '.join(info['course'])}")

    elif choose == 3:
        searchStudent = input("Enter name of student: ").lower()
        if searchStudent in studentInfo:
            info = studentInfo[searchStudent]
            print(f"{searchStudent.capitalize()} | Age: {info['age']} | Courses: {', '.join(info['course'])}")
        else:
            print("⚠️ Student not found!")

    elif choose == 4:
        searchStudent = input("Enter name of student: ").lower()
        if searchStudent in studentInfo:
            changeCourse = input("Enter new course: ").upper()
            print("Former courses:", ", ".join(studentInfo[searchStudent]['course']))
            studentInfo[searchStudent]['course'] = [changeCourse]
            save_data()
            print(f"✅ Updated courses for {searchStudent.capitalize()} to {changeCourse}")
        else:
            print("⚠️ Student not found!")

    elif choose == 5:
        searchStudent = input("Enter name of student: ").lower()
        if searchStudent in studentInfo:
            addCourse = input("Enter added course: ").upper()
            studentInfo[searchStudent]['course'].append(addCourse)
            save_data()
            print(f"✅ {searchStudent.capitalize()} now enrolled in {', '.join(studentInfo[searchStudent]['course'])}")
        else:
            print("⚠️ Student not found!")

    elif choose == 6:
        searchStudent = input("Enter name of student to delete: ").lower()
        if searchStudent in studentInfo:
            del studentInfo[searchStudent]
            save_data()
            print(f"✅ Deleted {searchStudent.capitalize()} from student records.")
        else:
            print("⚠️ Student not found!")

    elif choose == 7:
        print("✅ Exiting program...")
        save_data()
        sys.exit()

    else:
        print("⚠️ Invalid option. Please choose between 1 and 7.")

'''



             
