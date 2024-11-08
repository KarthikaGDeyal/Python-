newlist=[10,20,30,40,100]
print(len(newlist))
max=newlist[0]
for i in range(len(newlist)):
    if newlist[i]>max:
        max=newlist[i]
print(max)