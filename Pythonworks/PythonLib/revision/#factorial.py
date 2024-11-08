x=int(input("enter the no:"))
factorial=1
if x<0:
    print('enter a positive integer')
elif x==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,x+1):
        factorial=factorial*i
    print("factorial is",factorial)