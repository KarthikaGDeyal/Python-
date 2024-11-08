x={"Name":"Aryan","Age":23,"Place":"Cochin","Course":"Python"}
print("Name:",x["Name"])
print("Age:",x["Age"])

x["College"]="MES"
print(x)

x["Name"]="Rohan"
print(x)

del x["Age"]
print(x)