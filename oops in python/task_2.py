# Write a class “Calculator” capable of finding square, cube and square root of a number.


class Calculator:
    def __init__(self,number,power):
        self.number = number
        self.power = power

        # Calculation
        cal = number ** power
        print(f"Answer: {cal}")



while True:
    number = int(input("Enter number: "))
    power = int(input("Enter power: "))

    Calculator(number,power)