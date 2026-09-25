# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,number,power):
        self.number = number
        self.power = power

        # Calculation
        cal = number ** power
        print(f"Answer: {cal}")
    @staticmethod   
    def greet():   # dont need self because of staticmethod
        print("programm end")



while True:
    number = int(input("Enter number: "))
    power = int(input("Enter power: "))

    c1 = Calculator(number,power)
    c1.greet()

