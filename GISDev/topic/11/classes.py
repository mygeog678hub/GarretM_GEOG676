class Car:
    def __init__(self):
        pass

    def setColor(self, newColor):
        self.color = newColor

    def honkHorn(self):
        print("Beep beep")

myCar = Car()

myCar.setColor("red")

print(myCar.color)

myCar.honkHorn()