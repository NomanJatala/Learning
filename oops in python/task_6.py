# 6. Can you change the self-parameter inside a class to something else (say “noman”)? Try
# changing self to “slf” or “noman” and see the effects.


class Student:
    def __init__(noman,text):  # wring some thing else at the place of self
        noman.text = text

    def show(noman):
        print(noman.text)
    


s1 = Student("This is name string")

s1.show()