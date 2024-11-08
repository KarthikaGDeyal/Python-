num=int(input("enter the value :"))
i=2
n=0
while i<num:
    if num%i==0:
        n=1
        break
    i+=1
if n==0:
    print(num,"is a prime no")
elif n==1:
    print(num,"is not a prime no")
else:
    print("hi")