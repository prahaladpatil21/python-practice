#Implement a shape and derive circle and rectangle classes with a method calculate area each class should calculate area differently based on its shape
# create a loop to calculate areas for circle and rectangle objects


class Shape:
    def calculate(self):
        print("Area created")

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def calc_area(self):
        print(f"area of circle is:{(22/7)*self.radius*self.radius}")

class rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def calc_area(self):
        print(f"area of the rectangle: {self.length*self.width}")

c=Circle(5)
c.calc_area()