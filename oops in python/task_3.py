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