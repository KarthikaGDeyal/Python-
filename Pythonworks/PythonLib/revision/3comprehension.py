list1=["arya","diya","sujin"]
list2=[]
for i in list1:
    if "a" in i:
        list2.append(i)
print(list2)

list1=["arya","diya","sujin"]
list2=[x for x in list1 if "a" in x]
print(list2)