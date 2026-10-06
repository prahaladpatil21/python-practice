def discount_calculator(price):
    if price>0 and price<=1000:
        return (price*20)/100
    elif price >1000 and price <= 5000:
        return (price*25)/100
    elif price>5000 and price<=10000:
        return (price*30)/100
    elif price>10000:
        return (price*40)/100
print(discount_calculator(1000))