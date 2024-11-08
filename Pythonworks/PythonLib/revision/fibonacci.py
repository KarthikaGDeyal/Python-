num=int(input("enter the no of fibonacci series:"))
a=0
b=1
for i in range(0,num):
    print(a,end= " ")
    c=a+b
    a=b
    b=c