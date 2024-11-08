mylist=[1,2,3,4,5,6,3,3,1,2,5]
print("length of mylist is:",len(mylist))
newlist=[]
for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if mylist[i]==mylist[j] and mylist[i] not in newlist:
            newlist.append(mylist[i])
print(newlist)