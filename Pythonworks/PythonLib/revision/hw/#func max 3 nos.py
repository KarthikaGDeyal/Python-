def max(n1,n2,n3):
    if n1>n2 and n1>n3:
        print("n1 is larger")
    elif n2>n1 and n2>n3:
        print("n2 is larger")
    else:
        print("n3 is larger")
a=int(input("enter a :"))
b=int(input("enter b:"))
c=int(input("enter c :"))
max(a,b,c)