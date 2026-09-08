# Student marks system
students = {}
st = """
options:
Enter 1 to Add student
Enter 2 for view records
"""
def add_student():
    name = input("Enter student Name: ")
    marks = input("Enter marks")
    students[name] = marks

def show_records():
    for s,m in students.items():
        print(f'{s} : {m}')
        

while True:
    print(st)
    choice = int(input("Enter number: ")) 
     
    if choice ==1 :  
       add_student()
    elif(choice == 2):
        show_records()
        