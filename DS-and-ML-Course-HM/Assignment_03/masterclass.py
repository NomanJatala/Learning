# Student managment system
class Student:
    def __init__(self,name,student_id,age):

        self.name = name
        self.student_id = student_id
        self.age = age

    def show(self):
        print(f"""
ID : {self.student_id}
Name : {self.name}
Age : {self.age}""")

students = []
# Adding new Studnet to list
def add_student():
    try:
        student_id = int(input("Enter Student id: "))
        name = input("Enter Student name: ")
        age = int(input("Enter Student age: "))

        student = Student(name, student_id, age)

        students.append(student)
        print("Student added")
    except ValueError:
        print("Invalid input. Please enter valid data.")

# Showing Studnets
def view_students():
    if not students:
        print("No student found")
    for student in students:
        student.show()

def search_student():
    try:
        search_id = int(input("Enter student id to search: "))
        found = False
        for student in students:
            if student.student_id == search_id:
                student.show()
                found = True
                break
        if not found:
            print("Student not found")
    except ValueError:
        print("Enter valid search id")


while True:
    print(f"""
    1. Add Student
    2. View Students
    3. search studnet
    4. exit """)
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("Invalid choice. Please try again.")