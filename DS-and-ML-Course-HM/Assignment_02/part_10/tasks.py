a = 10
try:
    print(a/0)
except ZeroDivisionError:
    print("Any number cant be divided to zero")


try: 
    print(a/0)
except ZeroDivisionError:
    print("Any number cant be divided to zero")
except ValueError:
    print("Value is ")