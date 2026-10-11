vowels="aeiou"
s=input("sentence-->")
count=0
for ch in s:
    if ch in vowels:
        count+=1
print("vowels:",count)