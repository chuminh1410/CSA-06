class Square:
    def __init__ (self,long):
        self.long = long
    def cal_area(self):
        return self.long * 2

class Cube:
    def __init__ (self,long):
        self.long = long
    def cal_area(self):
        return 6 * self.long ** 2
    def cal_volume(self):
        return self.long ** 3


square = Square(2)
print('Square area:', square.cal_area())


cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())

