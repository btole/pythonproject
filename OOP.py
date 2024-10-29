class Fruits:
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
    def display(self):
        print(f"i love eating {self.name}, It costs sh{self.price}, and it is {self.color} in color")

test = Fruits("mango",10,"yellow")
test.display()

