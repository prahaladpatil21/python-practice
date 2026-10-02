'''bus_pass=int(input("enter the age-->"))
if bus_pass<=5 and bus_pass>0:
    print("free pass")
elif bus_pass>=60 and bus_pass<=100:
    print("senior citizen discoumt")
else:
    print("pay full fee")'''
'''write a pgm for pass eligiblity if they are below 5 years free pass
and greater then 60 years senior citizen pass and 
rest pay full payment'''

''''meal_time=int(input("enter the meal time-->"))  #24 hrs
if meal_time<=24:
    if meal_time==8:
        print("breakfast time!")
    elif meal_time==13:
        print("lunch time!")
    elif meal_time==20:
        print("dinner time")
    else:
        print("not a meal time")'''
#meal time checker with nested if else statements

age=int(input("enter the age-->"))
if age<=110:
    if age<=18:
        print("student membership")
    elif age>=60:
        print("senior citizen membership")
    else:
        print("reguler membership")