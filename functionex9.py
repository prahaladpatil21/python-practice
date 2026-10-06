
def parking_fee(hours):
    if hours>=0 and hours<=2:
        print("fee--$20")
        return True
    elif hours>=3 and hours<=5:
        print("fee--40")
        return True
    elif hours>=5:
        print("fee--70")
        return True
print(parking_fee(8))
#parking fees payment