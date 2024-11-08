x="HiAll"
lower=0
upper=0
for i in x:
    if (i.islower()):
        lower+=1
    else:
        upper+=1
print("no of lowercase",lower)
print("no of uppercase",upper)
