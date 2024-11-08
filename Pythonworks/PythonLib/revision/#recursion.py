def factorial_recursion(n):
    if n==1:
        return n
    else:
        return n*factorial_recursion(n-1)
num=int(input("enter the value of num:"))
if num<0:
    print("enter a positive no")
elif num==0:
    print("factorial of zero is 1")
else:
    print("factorial is:",factorial_recursion(num))
