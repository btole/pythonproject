class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print(f"{self.name} is {self.age} years and is a {self.gender}")

obj = Person("Tom",22,"Male")
obj.display()