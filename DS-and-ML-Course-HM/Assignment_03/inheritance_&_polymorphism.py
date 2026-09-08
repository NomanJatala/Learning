class Student:

    def __init__(self, name, age, class_name, student_id):
        self.name = name
        self.age = age
        self.class_name = class_name
        self.__student_id = student_id

    def set_student_id(self, new_id):
        self.__student_id = new_id

    def get_student_id(self):
        return self.__student_id

    def get_info(self):
        print(
            {
                "Name": self.name,
                "Age": self.age,
                "Class": self.class_name,
                "Student ID": self.__student_id,
            }
        )

class Teacher(Student):
    def __init__(self, name, age, class_name, student_id, subject):
        Student.__init__(self, name, age, class_name, student_id)
        self.subject = subject

    def get_info(self):
        print(
            {
                "Name": self.name,
                "Age": self.age,
                "Department": self.class_name,
                "Teacher ID": self.get_student_id(),
                "Subject": self.subject,
            }
        )

s1 = Student("Salman", 10, "8th", 4)
s1.get_info()

t1 = Teacher("Noman", 20, "BSAI", 50, "Python")
t1.set_student_id(20)
t1.get_info()