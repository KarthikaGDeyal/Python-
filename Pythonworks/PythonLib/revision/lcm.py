a=int(input("enter a:"))
b=int(input("enter b:"))
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        print("lcm is",i)
        break
