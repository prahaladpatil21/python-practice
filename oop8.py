#Create a class BankAccount with a private attribute balance
#write a getter method to retrieve the balance and a setter method to updateit, ensuring the balance never goes below zero 

class BankAccount:
    def __init__(self, balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, updated_balance):
        if updated_balance<0:
            print("ERROR")
            return 
        self.__balance=updated_balance

