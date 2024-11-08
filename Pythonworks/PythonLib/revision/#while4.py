n=int(input("enter a no:"))
while n>0:
    if n%2==0:
        print("even")
        break
    else:
        print("odd")
        break

print("odd nos are:")
i=1
while i<=100:
    if i%2!=0:
        print(i)
    i=i+1