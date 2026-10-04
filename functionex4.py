def calculator(a,b):
    return a+b, a-b, a*b, a/b,
print(calculator(10,20))#positional arguement
print(calculator(b=20,a=10))#keyword arguement

#simple calculator 


def count_digits(n):
    count=0
    
    while n>0:
        
        count=count+1
        n=n//10
    return count
print(count_digits(123456))
#calculate the number of digits