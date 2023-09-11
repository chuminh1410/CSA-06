import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("No real solutions")
elif delta == 0:
    x = -b / (2*a)
    print(f"Single real solution: x = {x}")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Two real solutions: x1 = {x1}, x2 = {x2}")
