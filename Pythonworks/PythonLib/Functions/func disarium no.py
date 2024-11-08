def calc_length(n):
    length=0
    while (n!=0):
        length+=1
        n//=10
    return length
num=int(input("enter the value of num:"))
# print("length is :",calc_length(num))
len=calc_length(num)
sum=0
rem=0
temp=num
while num>0:
    rem=num%10
    sum=sum+rem**len
    num//=10
    len-=1
if sum==temp:
    print("disarium")
else:
    print("not disarium")