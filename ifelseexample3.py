'''balance=50000
withdraw=int(input("enter amount to withdraw-->"))
remaining_amount=balance-withdraw
if withdraw<=0:
    print("INVALID AMOUNT!!")
elif withdraw>balance:
    print("insufficient balance")
else:
    print(f"remaining amount is {remaining_amount}") 
    #ask for account balance and withdraw amount'''




#ELECTRICITY BILLS
units=int(input("enter the units::"))
if units<=100:
    print(units*5)
elif units>100 and units<=200:
    print(units*7)
elif units>200:
    print(units*10)