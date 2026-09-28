marks=int(input("ENTER THE MARKS-->"))
if marks > 100 or marks <0:
    print("INVALID MARKS")
elif marks >= 90 and marks <=100:
    print("grade A")
elif marks >= 75 and marks <= 89:
    print("grade b")
elif marks >= 60 and marks <= 74:
    print("grade c")
elif marks >= 40 and marks <= 59:
    print("grade d")
elif marks <= 40:
    print("fail")

""" input marks
solve the given grade using if else elif 
and also reject below 0 and above 100 marks"""




number=int(input("ENTER THE NUMBER-->"))
if number > 0 and number % 2 ==0:
    print("number is positiva and even")
elif number  > 0 and number % 2!=0:
    print("number is positiva and odd")
elif number < 0 and number % 2 ==0:
    print("number is negative and even")
elif number < 0 and number % 2!=0:
    print("number is negative and odd")
else:
    print("number is zero")



#even/odd + positive/negative