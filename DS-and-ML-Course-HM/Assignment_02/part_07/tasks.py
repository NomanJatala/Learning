student = {"name":"Noman",
           "age":18,
           "Grade":"A"}

# access and update values
student["name"]= "Noman Tahir"
student["Grade"]= "A+"
student["age"] = 19
# print(student)

# Loop through dictionary items 
for key , value in student.items():
    print(f"{key} , {value}")