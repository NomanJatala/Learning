print("Student Registration")

while True:
    name = input("Enter name: ")
    email = input("Enter email: ")
    while "@" not in email or "." not in email or " " in email:
        email = input("Please enter a valid email: ")
    password = input("Enter password: ")
    while len(password) <8 or not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
        password = input("Enter a valid password: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{email},{password}\n")
    print("Student added in file") 