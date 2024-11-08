n=int(input("enter a no:"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if sum==n:
    print("armstrong no")
else:
    print("not armstrong no")