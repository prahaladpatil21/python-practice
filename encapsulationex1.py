class BankAccount:
    def __init__(self,account_no, balance):
        self.__account_no=account_no  #private attribute
        self.__balance=balance  #private attribute


    def check_balance(self):
        print(f"current balance is {self.__balance}")

    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount

        else:
            print("amount is invalid")

    def withdraw(self, amount):
        if self.__balance>amount:
            print("withdraw successfull")

        else:
            print("insufficient balance")

a1=BankAccount("565652356",2000)
a1.withdraw(500)
a1.deposit(500)
a1.check_balance()
