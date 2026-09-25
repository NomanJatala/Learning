class Programmers:
    def __init__(self,name,sallery,age):
        self.name = name
        self.sallery = sallery
        self.age = age
    def get_info(self):
        print(f"""
Name : {self.name}
Sallery : {self.sallery}
Age : {self.age}
""")
p1 = Programmers("Noman",45000,20)
p1.get_info()