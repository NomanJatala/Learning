def isPrime(num):
    i = 2
    while i<num:
        if num%i == 0:
            return False
        i+=1
    
    return True

n = int(input("Enter number: "))
print(isPrime(n))