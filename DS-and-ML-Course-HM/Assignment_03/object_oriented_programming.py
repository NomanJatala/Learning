class Computer:
    def __init__(self, brand, model, processor, ram, storage):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")

c1 = Computer("hp", " gen","i5", 8, 256)
c1.display_specs()