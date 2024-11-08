number=int(input("enter a no:"))
sum=0
temp=number
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if number==sum:
    print("no is armstrong")
else:
    print("no is not armstrong")
