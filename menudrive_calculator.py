def menu():
    print("**--simple claculator--**")
    print("1.Addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
menu()
while(True):
    choice=int(input("Enter your choice-->"))
    if choice in {1,2,3,4}:
        a=int(input("enter the first number-->"))
        b=int(input("enter the second number-->"))


    if choice==1:
        print(a+b)

    elif choice==2:
        print(a-b)

    elif choice==3:
        print(a*b)

    elif choice==4:
        if b!=0:
            print(a/b)
        else:
            print("can't divide")
    elif choice==5:
        print("exiting..")
        break
    else:
        print("invalid choice")
