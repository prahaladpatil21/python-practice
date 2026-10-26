#create a class employee with attribute name,designation,salary [default value of salary is 30000]
#write a method that displays the dwtails of each employee
# create employee object with different values for name and designation and test the default salary behaviour
class Employee:
    def __init__(self, name, designation, salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary

    def display(self):
        print(f"name-->{self.name} designation-->{self.designation} salary is {self.salary}")

e1=Employee("ram", "manager")
e2=Employee("ravi","HR", 35000)
e3=Employee("laxman","assistant",31500)

e1.display()