import math
class Circle:
    def __init__(self, radius=3):
        self.radius = radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return math.pi*2*self.radius
class Rectangle:
    def __init__(self, length=7, breadth=9):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a+self.b+self.c)/2
        return math.sqrt(s((s-self.a)+(s-self.b)+(s-self.c)))
    def perimeter(self):
        return self.a+self.b+self.c
shape = Rectangle()
print(shape.area())
print(shape.perimeter())


