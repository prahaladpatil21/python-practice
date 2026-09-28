sub_1=int(input("enter first subject-->"))
sub_2=int(input("enter second subject-->"))
sub_3=int(input("enter third subject-->"))
avg=(sub_1+sub_2+sub_3)/3
if sub_1<35 or sub_2<35 or sub_3<35:
    print("fail")
else:
    if avg>85:
        print(f"distinction  {avg}")
    
    elif avg>=60 and avg<=84:
        print(f"FIRST CLASS  {avg}")
    elif avg>=50 and avg<=59:
        print(f"SECOND CLASS {avg}")
    elif avg>35 and avg<=40:
        print(f"pass  {avg}")
