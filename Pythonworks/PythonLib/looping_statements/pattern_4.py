rows=int(input("enter the no:"))
space=rows
for i in range(1,rows+1):
    for s in range(space):
        print(end=" ")
    space=space-1
    for j in range(i+1):
        print("*" , end= " ")
    print()




















































