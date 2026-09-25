# Create a class with a class attribute a; create an object from it and set ‘a’ directly using
# ‘object.a = 0’. Does this change the class attribute?

class Person:
    name = "Noman"

    def set(self,name):
        self.name = name


p1 = Person()
print(p1.name)

# setter
p1.set("Sarmad")

# After set the value of name
print(p1.name)