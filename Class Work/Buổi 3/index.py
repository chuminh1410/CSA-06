class Person:
    def __init__(self, height, weight, colour):
        self.height = height
        self.weight = weight
        self.colour = colour
        self.salary = 1 
nguoi1 = Person(input("height :"),input("weight:"),input("skin color :"))

class Dev:
    def __init__(self, height, weight, colour, position, language):
        self.height = height
        self.weight = weight
        self.colour = colour
        self.salary = 1.02
        self.position = position
        self.language = language
dev1 = Dev(input("height :"),input("weight :"),input("skin color :"),input("hsl :"),input("position:"),input("language :"))

class Manager:
    def __init__(self, height, weight, colour, position, chuc_vu):
        self.height = height
        self.weight = weight
        self.colour = colour
        self.position = position
        self.chuc_vu = chuc_vu
manager1 = Manager(input("height :"),input("weight :"),input("skin color :"),input("hsl :"),input("position :"),input("chuc vu :"))