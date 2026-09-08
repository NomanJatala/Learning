email = input("Enter email: ")
password = input("Enter password: ")

with open("students.txt","r") as file:
    for line in file:
        s_name, s_email, s_password = line.strip().split(",")

        if email == s_email and password == s_password:
            print("Login successful")
            break
        else:
            print("Login fail")