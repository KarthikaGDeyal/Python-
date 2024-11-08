a=[1,2,3,4,5,3,2,1]
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j] and a[i] not in b:
            b.append(a[i])
print(b)