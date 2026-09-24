sec=int(input("enter the seconds-->"))
hours=sec//3600
minutes=(sec%3600)//60
seconds=(sec%60)
print(f"{hours} : {minutes} : {seconds}")