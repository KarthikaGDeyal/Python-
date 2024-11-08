list1=[1,2,3,4,5]
list2=[3,4,5,6,7,8,3,4,3,3]
result=[]
for i in list1:
    for j in list2:
        if i==j and i not in result:
            result.append(i)
print(result)