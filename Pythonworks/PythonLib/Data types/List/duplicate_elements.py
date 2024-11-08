mylist=[1,2,3,4,5,67,8,7,65,1,2]
newlist=[]
print("length of mylist is:",len(mylist))
for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if  mylist[i]==mylist[j] and mylist[i] not in newlist:
            newlist.append(mylist[i])
print(newlist)
    