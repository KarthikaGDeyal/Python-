rows=int(input("enter the no:"))
for i in range(rows+1,0,-1):
    for j in range(0,i-1):
        print("*",end= " ")
    print()