x=int(input("enter x:"))
factorial=1
if x<0:
    print("please enter a positive integer")
elif x==0:
    print("factorial is 1")
else:
    for i in range(1,x+1):
        factorial=factorial*i
    print("factorial is",factorial )