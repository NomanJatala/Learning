lst = [3,4,5,2,5,5,6,9,4,2,5,11]
lst.append(45)
print(lst)
print(lst[0])
print(lst[-1])
print(lst[1:3])

lst[4] = 44
print(lst)

# --
print("List Method")
print(lst)
lst.insert(1,4)  # for inserting item at specific index
lst.remove(5)  # for removing item form list
print(lst.pop())   # for removing last item form list
print(lst.index(4))