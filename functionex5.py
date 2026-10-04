def check_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=75 and marks<=89:
        return "B"
    elif marks>=60 and marks<=74:
        return "c"
    elif marks<60:
        return "Fail"
print(check_grade(78))
#grade checker

def num(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"
print(num(96))
#check number is positive, zero or negative
    