import math

class Shape:
    def __init__(self, color):
        self.color = color

    def getArea(self):
        pass


class Rectangle(Shape):

    def __init__(self, color):
        Shape.__init__(self, color)

    def setLength(self, length):
        self.l = length

    def setWidth(self, width):
        self.w = width

    def getArea(self):
        return self.l * self.w


class Circle(Shape):

    def __init__(self, color, radius=None):
        Shape.__init__(self, color)
        self.r = radius

    def setRadius(self, radius):
        self.r = radius

    def getArea(self):
        return math.pi * self.r * self.r


shape1 = Shape("blue")
shape2 = Rectangle("red")
shape2.setLength(3)
shape2.setWidth(4)

print(shape2.getArea())


shape3 = Circle("orange")
shape3.setRadius(5)

print(shape3.getArea())


shape4 = Circle("orange", 2)

print(shape4.getArea())