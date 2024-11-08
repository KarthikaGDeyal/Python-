list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def addition(a,b):
    return a+b
c=list(map(addition,list1,list2))
print(c)

a=[1,2,3]
b=[4,5,6]
def addition(x,y):
    return x+y
c=list(map(addition,a,b))
print(c)
