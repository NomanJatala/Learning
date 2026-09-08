

def sqr(n):
    return n*n
def bigger(n,m):
    if n > m:
        return n
    elif m > n:
        return m

print(sqr(5))
print(bigger(2,3))

# args and kwargs

def add_numbers(*args):
    return sum(args)

def student_system(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

add_numbers(1,2,3,4,5)
student_system(name= "Noman",age = 20)