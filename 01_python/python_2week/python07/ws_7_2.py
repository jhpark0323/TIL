# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def calculate_area(self):
        return self.width * self.length


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)