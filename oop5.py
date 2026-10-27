#create a class BankAccount with private attribute for account number and balance
#Add method to check balance,deposite and withdraw funds
#Try accesing the balance directly and observe the result
class BankAccount:
    def __init__(self, account_number, Balance):
        self.__account_number=account_number
        self.__Balance=Balance

    def check_balance(self):
        print(self.__Balance)
    def deposit(self, amount):
        self.__Balance+=amount

    def withdraw(self, amount):
        if self.__Balance<amount:
            print("insufficient balance")
        self.__Balance-=amount 
        print(f"withdraw successful - balance:{self.__Balance}")

a=BankAccount(account_number=1234, Balance=10000)
a.withdraw(1000)
a.check_balance()