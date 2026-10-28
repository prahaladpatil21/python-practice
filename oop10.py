#create a parent class shape with a method draw() that prints("DRawing shape")
#create child class Circle that overrides draw() to print("drawing circle")
class Shape:
    def draw(self):
        print("Drawing A Shape")

class Circle(Shape):
    def draw(self):
        super().draw()
        print("Draw Circle")
c=Circle()
c.draw()

