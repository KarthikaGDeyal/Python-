x=["Ashika","Sharon","Vishnu","Anna",978654,98765467,234567,[1,2,3,4,5]]
print("Our list is:",x)
print(x[0])
print(x[-1])
print(x[-2])

x.insert(0,"libina")
print(x)

list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
list1.append(list2)
print(list1)

list3=[1,2,3,4,5]
list4=[3,4,5,6,7]
list3.insert(0,list4)
print(list3)

a=[11,12,13,14,15]
b=[1,2,3,4,5]
a.extend(b)
print(a)


p=[2,5,3,88,55,90,78]
q=[98,234,23,654,21]
print(p+q)