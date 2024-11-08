a=lambda p,q:p+q
print(a(3,2))

p=lambda i:i**2
print(p(10))

num1=int(input("enter value of num1:"))
num2=int(input("enter value of num2:"))
p=lambda a,b:a+b
print("sum=",p(num1,num2))

x=int(input("enter value of x:"))
y=int(input("enter value of y:"))
difference=lambda a,b:a-b
print("difference=",difference(x,y))