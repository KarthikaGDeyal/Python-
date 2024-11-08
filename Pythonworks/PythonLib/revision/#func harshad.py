num=int(input("enter a no:"))
sum=0
rem=0
temp=num
while num>0:
    rem=num%10
    sum=sum+rem
    num//=10
if temp%sum==0:
    print("harshad no")
else:
    print("not harshad no")