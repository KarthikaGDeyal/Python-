from math import sqrt
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
r=b**2-4*a*c
if r>0:
    x1=((-b)+sqrt(r))/2*a
    x2=((-b)-sqrt(r))/2*a
    print("roots are",x1,x2)
elif r==0:
    x3=(-b)/2*a
    print("root is",x2)
else:
    print("no roots")














