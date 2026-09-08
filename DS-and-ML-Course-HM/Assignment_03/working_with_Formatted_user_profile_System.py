class CreateUserProfile:
    def __init__(self, id, name, email, age):
        self.id = id
        self.name = name.title()
        self.email = email.lower()
        self.age = age.strip()

        profile_data = f""" 
ID: {self.id}
Name: {self.name}
Email: {self.email}
Age: {self.age} 
 -------------------

 """
        with open("file_handling_files/user_profile.txt", "a") as file:
            file.write(profile_data)
        print("User profile created successfully! \n")

user_if = 1

while True:
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")
    user_profile = CreateUserProfile(user_if, name, email, age)

    user_if += 1

    choice = input("Do you want to create another profile? (yes/no): ")
    if choice.lower() != "yes":
        print("Goodbye!")
        break