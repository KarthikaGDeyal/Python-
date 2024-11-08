def calc_len(n):
    length=0
    while n!=0:
        length+=1
        n//=10
    return length
num=int(input("enter a no:"))
len=calc_len(num)
sum=0
rem=0
temp=num
while temp>0:
    rem=temp%10
    sum+=rem**len
    temp=temp//10
    len-=1
if sum==num:
    print('disarium no')
else:
    print("not disarium no")