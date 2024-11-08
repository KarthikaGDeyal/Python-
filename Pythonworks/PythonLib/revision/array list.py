x=["ASHIKA","sharon","vishnu","anna",978654,97865467,234567,[1,2,3,4,5]]
print(x)
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
list4=[6,7,8,9,10]
list3.insert(0,list4)
print(list3)

a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)

p=[10,12,13,14,15]
q=[16,17,18,19,20]
print(p+q)