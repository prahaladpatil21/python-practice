#create a base class Vehicle with start method then create a subclass Bike with an additional ride() method
#Demonstrate how the Bike can use start and ride
class Vehicle:
    def start(self):
        print("vehicle is starting")

class Bike(Vehicle):
    def __init__(self, name):
        self.name=name

    def ride(self):
        print("riding")

b=Bike("splender")
b.start()
b.ride()