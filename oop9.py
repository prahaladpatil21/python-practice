#write a class calculator with a method multiply() allow it to take either two or three arguments to multiply two or three numbers 

class Calculator:
    def __init__(self, a, b, c=1):
        self.a=a
        self.b=b
        self.c=c

    def multiply(self):
        print(f"multipled:{self.a*self.b*self.c}")

x=Calculator(2, 3)
x.multiply()