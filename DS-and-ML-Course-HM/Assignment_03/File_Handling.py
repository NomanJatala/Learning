
#  writing
with open("file_handling_files/students.txt", "w") as stu_file:
    w_stu = stu_file.write("This text is write by .write mode")
    print(w_stu)


with open("file_handling_files/data.txt", "w") as data_file:
    data_file.write("This text is write by .write mode")
    print("Data file is created and text is written in it")

with open("file_handling_files/students.txt", "r") as stu_file:
    con_stu = stu_file.read()

    
with open("file_handling_files/data.txt", "r") as data_file:
    con_data = data_file.read()
    print(con_data)

    print(con_stu) 