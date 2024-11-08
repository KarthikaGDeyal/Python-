number=int(input("enter the no:"))
temp=number
sum=0
if number<=0:
    print("please enter a positive integer")
else:
    while number>0:
        sum+=number
        number-=1
    print("Sum of",temp,"natural nos is",sum)