n=int(input("enter the nos:"))
sum=0
start=2
for i in range(0,n):
    print(start,end= "+")
    sum=sum+start
    start=start*10+2
print("\n sum is",sum)
