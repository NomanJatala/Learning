def log_error(error):
    with open('file_handling_files/error_log.txt', 'a') as file:
       file.write(f"{error}\n")

def safe_cal():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
        else:
            raise ValueError("Invalid operator")
        print(f"Result: {result}")
    except Exception as e:
        print(f"error : {e}")
        log_error(e)

    finally:
        print("execution completed.")

while True:
    print("----safe calculator----")
    safe_cal()
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break