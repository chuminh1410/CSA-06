import math

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
    def area(self):
        return self.height * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius**2

def main():
    shape = input("Shape (rectangle|circle): ")
    
    if shape == "rectangle":
        height = float(input("Height: "))
        width = float(input("Width: "))
        shape_obj = Rectangle(height, width)
    elif shape == "circle":
        radius = float(input("Radius: "))
        shape_obj = Circle(radius)
    
    perimeter = shape_obj.perimeter()
    area = shape_obj.area()
    
    print(f"=> Perimeter: {perimeter:.2f}")
    print(f"=> Area: {area:.2f}")

if __name__ == "__main__":
    main()
