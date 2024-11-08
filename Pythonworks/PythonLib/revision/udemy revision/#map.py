list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def addition(x,y):
    return x+y
c=list(map(addition,list1,list2))
print(c)