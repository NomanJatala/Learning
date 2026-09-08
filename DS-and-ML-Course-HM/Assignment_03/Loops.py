# use of continue statement

print("Continue statement example:")
for i in range(5):
    if i == 3:
        continue
    print(i)

# use of break statement
print("Break statement example:")
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1

# nested loops
print("Nested loops example:")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

#  Multiplication table using  loops
print("Multiplication table:")
input_number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{input_number} x {i} = {input_number * i}")
