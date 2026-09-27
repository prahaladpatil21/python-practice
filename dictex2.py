mobile={"brand":"samsung",
        "model 1":"S24",
        "price":65000
        }
mobile["STORAGE"]="256GB"
mobile.pop("price")
print(mobile)

'''add and remove
add storage=256 gb remove price 
print all the final dictionary'''

college={
    "Student":{
        "name":"arun",
        "age":20
    },
    "course":{
        "name":"cse",
        "year":2
    }
}
print(college["Student"]["name"])
print(college["Student"]["age"])
print(college["course"]["name"])
print(college["course"]["year"])