lower_value=int(input("enter the lower value:"))
upper_value=int(input("enter the upper value:"))
for num in range(lower_value,upper_value+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp=temp//10
    if sum==num:
        print(num)
