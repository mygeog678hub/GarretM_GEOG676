# Attributes
class Truck:
    numOfWheels = 4 # This is an example of a class attribute; all instances of Truck have 4 wheels
    def __init__(self, color):
        self.color = color # This is an example of an instance attribute; only some instances will have a color attribute (that is, if it was created like so `chevy = Truck('green')`

chevy = Truck('Green')
chevy.color = 'Green' # This is another example of an instance attribute
chevy.tinted = True # This is an example of an instance variable defined outside the class
print(chevy.numOfWheels) # This prints our class attribute numOfWheels
print(chevy.color)

class Vehicle:
    numOfWheels = 4
    def __init__(self):
        pass

class Truck(Vehicle):
    def __init__(self):
        pass

ford = Truck()
print(ford.numOfWheels)  # Whenever we create a subclass (i.e. create a new descendent class) we are also including any class attributes of the parent class (aka inheritance). In the example below, object ford is of type Truck which does not have a class attribute numOfWheels declared. Yet when we run this snippet we still get a print out of 4. This is because Truck is a subclass of Vehicle and all class attributes of Vehicle also belong to Truck.