a=int(input("enter a:"))
b=int(input("enter b:"))
while a%b!=0:
    rem=a%b
    a=b
    b=rem
print("hcf is",b)