mydict={1:"abc",2:"def",3:"ghi"}
print(mydict)
print(mydict[1])
print(mydict[2])

x={"name":"diya","age":23,"place":"cochin","course":"cc"}
print("name:",x["name"])
print("place:",x["place"])

x[4]="jkl"
print(x)

x["name"]="nia"
print(x)

del x["name"]
print(x)

mydict={
    "Name":"Aryan",
    "Age":23,
    "Place":"Cochin",
    "Course":"Python"
}

for i in mydict.keys():
    print(i)

for i in mydict.values():
    print(i)
    
for i in mydict.items():
    print(i)
