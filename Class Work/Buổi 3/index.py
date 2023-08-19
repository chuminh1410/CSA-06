class Person:
    def __init__(self, height, weight, colour):
        self.height = height
        self.weight = weight
        self.colour = colour
        self.salary = 1 

# nguoi1 = Person(input("\nheight :"),input("weight:"),input("skin color :"))
# print(f"\nPerson \n Height: {nguoi1.height}\n Weight: {nguoi1.weight} \n Skin color: {nguoi1.colour}\n")

class Dev(Person):
    def __init__(self, height, weight, colour, position, language):
        super().__init__(height,weight,colour)
        self.salary = 1.02
        self.position = position
        self.language = language
        
# dev1 = Dev(input("\nheight :"),input("weight :"),input("skin color :"),input("position:"),input("language :"))
# print(f"\nDev: \n Height: {dev1.height}\n Weight: {dev1.weight} \n Skin color: {dev1.colour} \n hsl: {dev1.salary}\n language: {dev1.language}")

class Manager(Person):
    def __init__(self,height,weight,colour,position,chuc_vu):
        super().__init__(height,weight,colour)
        self.hsl = 1.5
        self.position = position
        self.chuc_vu = chuc_vu
        
# manager1 = Manager(input("\nheight :"),input("weight :"),input("skin color :"),input("position :"),input("chuc vu :"))
# print(f"\nManager: \n Height: {manager1.height}\n Weight: {manager1.weight} \n Skin color: {manager1.colour} \n postition: {manager1.chuc_vu}\n chuc vu: {manager1.chuc_vu}")

def tinh_luong(person):
    if isinstance(person, Dev):
        return 1000 * person.salary
    elif isinstance(person, Manager):
        return 1000 * person.hsl
    else:
        return 1000 * person.salary

nguoi1 = Person("170cm", "60kg", "Yellow")
dev1 = Dev("175cm", "70kg", "White", "Developer", "Python")
manager1 = Manager("180cm", "80kg", "Black", "Manager", "Quản lý dự án")

print(f"Person Salary: {tinh_luong(nguoi1)}$")
print(f"Dev Salary: {tinh_luong(dev1)}$")
print(f"Manager Salary: {tinh_luong(manager1)}$")