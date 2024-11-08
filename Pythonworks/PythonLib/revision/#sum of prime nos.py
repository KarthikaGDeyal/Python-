lower_value=int(input("enter the value:"))
upper_value=(int(input("enter the value:")))
sum=0
for num in range(lower_value,upper_value+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        sum=sum+num
print(sum)
