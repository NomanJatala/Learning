try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is:", result)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") 