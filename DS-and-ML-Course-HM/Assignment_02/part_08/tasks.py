with open("sample.txt","w") as file:
    file.write("Hellow Noman")

#  Read
with open("sample.txt","r") as fileRead:
    show = fileRead.read()

print(show)

#  Append
with open("sample.txt","a") as fileAppend :
    fileAppend.write("this line is appened")