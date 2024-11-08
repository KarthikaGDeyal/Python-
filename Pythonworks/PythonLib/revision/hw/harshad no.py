n=int(input("enter a no:"))
sum=0
rem=0
temp=n
while temp>0:
    rem=temp%10
    sum+=rem
    temp=temp//10
if n%sum==0:
    print("harshad no")
else:
    print("not harshad no")
