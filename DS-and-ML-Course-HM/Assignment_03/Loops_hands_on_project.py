class MultiplicationTable:
    def __init__(self, number):
        self.number = number

    def display_table(self):
        for i in range(1, 11):
            print(f"{self.number} x {i} = {self.number * i}")

m1 = MultiplicationTable(5)
m1.display_table()