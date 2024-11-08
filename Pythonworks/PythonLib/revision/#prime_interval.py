lower_value=int(input("enter the lower value:"))
upper_value=int(input("enter the upper value:"))
print("prime nos in the range are:")
for num in range(lower_value,upper_value+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)