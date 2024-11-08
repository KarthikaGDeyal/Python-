from math import sqrt
a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
c=float(input("enter the value of c:"))
r=(b**2)-(4*a*c)
if r>0:
    x1=((-b)+sqrt(r))/2*a
    x2=((-b)-sqrt(r))/2*a
    print("the results are",x1,x2)
elif r==0:
    x3=(-b)/2*a
    print("the result is",x3)
else:
    print("there are no roots..!,descriminant less than zero")