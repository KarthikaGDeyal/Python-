for i in range(1,10):
    print(i)

    #
for i in range(1,10,3):
        print(i)

#odd nos
for i in range(1,21,2):
    print(i)

#even nos
for i in range(0,101,2):
    print(i)

#multiplication table
x=int(input("enter a no:"))
for i in range(1,11):
    print(x*i)

#swapping
x=int(input("enter a no:"))
y=int(input("enter a no:"))
print("before swapping the no is",x)
print("before swapping the no is",y)
z=x
x=y
y=z
print("after swapping the value of x is",x)
print("after swapping the value of y is",y)

#swapping without 3rd variable
x=int(input("enter x:"))
y=int(input("enter y:"))
print("before swapping value of x:",x)
print("before swapping value of y:",y)
x-=y
y=y+x
x=y-x
print("after swapping value of x:",x)
print("after swapping value of y:",y)

#sum of natural nos
x=int(input("enter a no:"))
sum=0
for i in range(0,x+1):
    sum=sum+i
print(sum)