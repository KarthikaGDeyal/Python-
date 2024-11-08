n=int(input("enter the no:"))
factorial=1
if n==0:
    print("factorial is 1")
elif n<0:
    print("enter a positive integer")
else:
    for i in range(1,n+1):
        factorial*=i
    print("factorial is",factorial)