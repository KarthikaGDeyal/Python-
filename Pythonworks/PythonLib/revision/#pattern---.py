n=int(input("enter the no of rows:"))
k=int(input("enter the no of colums:"))
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end= " ")
    print()