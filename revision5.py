dict={"dharwad":"pedha","belgavi":"kunda",
      "bagalkot":"bhaji","gokak":"kardhantu","badami":"temple"
      }
print(type(dict))
dict["mangalore"]="neer dose"
print(dict)
dict["badami"]="caves"
print(dict)
dict.pop("gokak")
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())

'''create dictionary of 5 cities and there famous food 
add a new city and famous food
update the value
get keys,values, and remove one city'''

dict2={
    "student1":{
    "name":"pratik",
    "fav_food":"paneer",
    "fav_fruit":"banana"
    },
    "student2":{
    "name":"ram",
    "fav_food" : "gobi",
     "fav_fruit":"mango"

    }
}
print(dict2["student2"]["fav_food"])

#nested dictionary
