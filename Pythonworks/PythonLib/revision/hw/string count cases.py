a=input("enter a string:")
lower=0
upper=0
for i in a:
    if i.islower():
        lower+=1
    else:
        upper+=1
print("no of lower cases:",lower)
print("no of upper cases:",upper)