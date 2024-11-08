def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("select your choice:")
print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
choice=input("enter your choice:")
num1=int(input("enter value of num1:"))
num2=int(input("enter value of num2:"))
if choice=="A" or choice=="a":
    print("sum=",addition(num1,num2))
elif choice=="B" or choice=="b":
    print("difference=",subtraction(num1,num2))
elif choice=="C" or choice=="c":
    print("multiplication=",multiplication(num1,num2))
elif choice=="D" or choice=="d":
    print("division=",division(num1,num2))
else:
    print("invalid syntax")