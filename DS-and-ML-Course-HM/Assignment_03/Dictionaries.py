dic = {
    "name": "Noman",
    "age" : 19,
    "semester": 3
}
print(dic)
print(dic["name"])
# adding new key and value in dictionary
dic["Department"] = "CS and IT"
print(dic)
# Dic are mutable
dic["age"] = 20
print(dic)
# Checking existence

print("name" in dic)
print("name" not in dic)

del dic["Department"]
print(dic)
print(dic.items())
print(dic.keys())
print(dic.values())