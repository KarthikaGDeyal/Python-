num=int(input("enter a number:"))
if num==1:
    print("1 is not a prime no")
elif num==0:
    print("you have entered zero")
elif num<0:
    print("please enter a positive integer")
else:
    for i in range(2,num):
        if num%i==0:
            print("num is not a prime no")
            break
    else:
        print("num is a prime no")