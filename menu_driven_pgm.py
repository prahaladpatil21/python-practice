#banking system example
print("banking system")
print("1.check balance")
print("2.deposit")
print("3.withdraw money")
print("4.exit")

balance=1000
while(True):
    choice=int(input("ENTER YOUR CHOICE-->"))
    print("you enterd choice",choice)

    if choice==1:
        print("balance:", balance)
    elif choice==2:
        amount=int(input("enter your amount to deposit:"))
        balance=balance+amount
        print("amount:",balance)

    elif choice==3:
        amount_withdraw=int(input("enter money to withdraw:"))
        if balance>=amount_withdraw:
            balance=balance-amount_withdraw
        print("withdraw successfull:",balance)

    elif choice==4:
        print("Exiting! thank you")
        break
    else:
        print("invalid choice please try again!")