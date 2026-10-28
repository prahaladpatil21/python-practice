#abstract class 


from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calc_salary(self):
        pass

class Manager(Employee):
    def calc_salary(self):
        print("managers salary calculated")

m1=Manager()
m1.calc_salary()