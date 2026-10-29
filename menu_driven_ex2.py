def menu():
    print("1.Add Student Details-->")
    print("2.Display Student Details")
    print("4.Exit")
menu()
while(True):
    choice=int(input("Enter your choice-->"))

    if choice==1:
        print("--student details are--")
        name=input("name=")
        age=int(input("age="))
        usn=input("usn=")

        print("student details added successfully")

    elif choice==2:
        print("student details are:")
        print("name:",name)
        print("age:",age)
        print("usn:",usn)

    elif choice==3:
        print("exiting..")
        break
    else:
        print("invalid choice!")