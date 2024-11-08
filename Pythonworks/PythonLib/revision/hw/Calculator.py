def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
print("select your choice:")
print("A.addition")
print("B.subtraction")
print("C.multiplication")
print("D.division")
choice=input("enter your choice:")
if choice=="a" or choice=="A":
    print("sum is:",addition(num1,num2))
elif choice=="b" or choice=="B":
    print("subtraction is:",subtraction(num1,num2))
elif choice=="c" or choice=="C":
    print("mutiplication is:",multiplication(num1,num2))
elif choice=="d" or choice=="D":
    print("division is:",division(num1,num2))
else:
    print("invalid syntax")
