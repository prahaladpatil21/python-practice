def is_even(num):
    if num % 2==0:
        print("even")
        return True
    else:
        print("odd")
        return False
        
print(is_even(2))

#print even numbers

def add_num(a,b):
    return(a+b)
add_num(5,8)#positional arguements
add_num(a=5,b=8)# keyword arguements
print(add_num(5,8))