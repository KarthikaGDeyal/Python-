n=int(input("enter n:"))
temp=n
x=n
count=0
while temp>0:
    temp=temp//10
    count=count+1
print(count)

sum=0
while x>0:
    rem=x%10
    sum=sum+rem**count
    x=x//10
    count=count-1
if sum==n:
    print(n,"disarium no")
else:
    print(n,"not disarium no")

