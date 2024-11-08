a=[1,2,3,4,5]
b=[2,3,6,7,8]
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)