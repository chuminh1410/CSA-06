class MathList:
    def __init__(self, values):
        self.values = values
    
    def __add__(self, num):
        new_values = [value + num for value in self.values]
        return MathList(new_values)
    
    def __sub__(self, num):
        new_values = [value - num for value in self.values]
        return MathList(new_values)
    
    def __str__(self):
        return str(self.values)

m_list= MathList([1, 2, 3, 4, 5])
print(m_list)

m_list += 2
print(m_list)
