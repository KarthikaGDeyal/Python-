x=int(input("enter x:"))
if x==1:
    print("1 is not a prime no")
elif x==0:
    print("you have entered zero")
elif x<0:
    print("enter a positive integer")
else:
    for i in range(2,x):
        if x%i==0:
            print("no is not prime")
            break
    else:
        print("no is prime")
