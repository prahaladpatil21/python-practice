def electricity_bill(units):
    if units>0 and units<100:
        return units*5
    elif units>=100 and units<=200:
        return units*7
    elif units>200:
        return units*10

print(electricity_bill(200)) 
#electricity bill