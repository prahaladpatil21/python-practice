def total(*args):
    sum=0
    for num in args:
        sum+=num
    return sum
print(total(1,2,3))