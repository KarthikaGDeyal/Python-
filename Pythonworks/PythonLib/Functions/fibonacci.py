n=int(input("enter num;"))
a=0
b=1
for i in range(0,n+1):
    c=a+b
    print(a,end=" ")
    a=b
    b=c