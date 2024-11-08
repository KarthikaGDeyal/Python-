def calculate_length(n):
    length=0
    while(n!=0):
        length+=1
        n//=10
    return length
num=int(input("enter num:"))
print("length is",calculate_length(num))