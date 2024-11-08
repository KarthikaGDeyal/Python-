num=int(input("enter the no:"))
if num==1:
    print("1 is not a prime no")
elif num==0:
    print("you have entered zero")
elif num<0:
    print("no is negative")
else:
    for i in range(2,num):
        if num%i==0:
            print("num is not prime")
            break
    else:
        print("num is prime")



















































