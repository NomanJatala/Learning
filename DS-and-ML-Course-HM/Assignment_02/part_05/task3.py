# Defalt parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Ali")

# *args
def add_numbers(*args):
    total = sum(args)
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(10, 20, 30, 40))

# **kwargs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Ali", age=25, city="Lahore")