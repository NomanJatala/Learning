class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


students = []

def load_data():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 3:
                    student = Student(data[0], data[1], data[2])
                    students.append(student)
    except FileNotFoundError:
        pass 

def save_data():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student.name},{student.age},{student.grade}\n")

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    student = Student(name, age, grade)
    students.append(student)
    save_data()
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n--- All Students ---")
        for i in range(len(students)):
            s = students[i]
            print(f"{i + 1}. Name: {s.name}, Age: {s.age}, Grade: {s.grade}")
        print("--------------------")

def update_student():
    view_students()
    
    if len(students) > 0:
        index = int(input("Enter student number to update: ")) - 1
        
        if 0 <= index < len(students):
            s = students[index]
            s.name = input("Enter new name: ")
            s.age = input("Enter new age: ")
            s.grade = input("Enter new grade: ")
            
            save_data()
            print("Student updated successfully!")
        else:
            print("Invalid number.")

def delete_student():
    view_students()
    if len(students) > 0:
        index = int(input("Enter student number to delete: ")) - 1
        
        if 0 <= index < len(students):
            students.pop(index)
            
            save_data()
            print("Student deleted successfully!")
        else:
            print("Invalid number.")

def main():
    load_data() 
    
    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. View all students")
        print("3. Update student info")
        print("4. Delete student")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break  
        else:
            print("Invalid choice. Please try again.")

main()