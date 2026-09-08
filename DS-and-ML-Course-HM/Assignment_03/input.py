print("Calculator")


value_1 = int(input("Please enter a number: "))
value_2 = int(input("Please enter a number: "))

choice = input("Choose an operation (+, -, *, /): ")
if choice == '+':
    result = value_1 + value_2
elif choice == '-':
    result = value_1 - value_2
elif choice == '*':
    result = value_1 * value_2
elif choice == '/':
    result = value_1 / value_2
else:
    result = "Invalid operation"

print(f"Result: {result}")