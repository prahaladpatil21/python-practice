
try:
    age=int(input("Enter the age-->"))
    if age>=0:
        print("age is valid")
        print(f"He/she will take {100-age} years to become 100 years old")
    else:
        print("age cannot be negative")
except Exception as e:
    print(f"error! please try again-{e}")

    
#age verifier ask the user for there age if the age is valid(number),
# show in how many years they will be 100 years old
# handle invalid input gracefully