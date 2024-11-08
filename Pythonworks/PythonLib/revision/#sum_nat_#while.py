num=int(input("enter the nos:"))
temp=num
sum=0
if num<=0:
    print("enter a positive integer")
else:
    while num>0:
        sum=sum+num
        num=num-1
    print("the sum of",temp,"natural nos is",sum)