class Vehicle:
    def start(self):
        print("vehicle starting")

class Bike(Vehicle):
    def ride(self):
        print("riding")

b=Bike()
b.start()

b.ride()
#create a base class vehicle with a start method then create subclass bike with an additional ride() method 
#demonstrate how the bike can use both start and ride