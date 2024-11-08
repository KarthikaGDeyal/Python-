
try:
    x = int(input("enter value of x:"))
    y = int(input("enter value of y:"))
    result = x / y
    print(x)
except:
    print("there is an error")
else:
    print("succesful division")
finally:
    print("division successful")