age=int(input("enter the age-->"))
if age <0 or age >110:
    print("INVALID AGE")
elif age >= 0 and age <=12:
    print("child")
elif age >=13 and age <=17:
    print("teenager")
elif age >=18 and age <=59:
    print("adult")
else:
    print("senior citizen")
    #age category




username=input("enter the username-->")
password=input("enter the password-->")
if username=="admin" and password=="1234":
    print("login successfull$$")
elif username!="admin" and password=="1234":
    print("wrong username!!")
elif username=="admin" and password!="1234":
    print("wrong password!!")
else:
    print("password and username are wrong!!")
    # username and password check

