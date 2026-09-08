class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

class Teacher(Student):
    def __init__(self, name, age, grade, subject):
        super().__init__(name, age, grade)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")