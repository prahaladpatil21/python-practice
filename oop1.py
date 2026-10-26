class mobile:
    def __init__(self, brand , price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"{self.brand} costs {self.price}")
m1=mobile("oppo", 20000)
m2=mobile("samsung",30000)

m2.display()
m1.display()
