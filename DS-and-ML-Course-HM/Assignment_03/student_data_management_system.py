import json
import os
path = 'file_handling_files/student.json'

def add_student():
    name  = input("Enter Name: ")
    age = int(input("Enter age: "))
    class_name = input("Enter Class name: ")
    
    new_student = {
        "name" : name,
        "age"  : age,
        "class_name" : class_name
        }
    
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "r") as file:
            students = json.load(file)
    else:
        students = []

    students.append(new_student)

    with open(path, "w") as file:
        json.dump(students, file, indent=4)


def view_students():
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "r") as file:
            data = json.load(file)
            print(data)
    else:
        print("No student data found.")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()
    if choice == 2:
          view_students()
    if choice == 3:
          break


