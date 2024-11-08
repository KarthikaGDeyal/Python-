try:
    x=int(input("enter value of x:"))
    y=int(input("enter value of y:"))
    result=x/y
    print(x)
except ZeroDivisionError:
    print("error occurred")
except ValueError:
    print("value error occurred")

#try except else
try:
    x = int(input("enter value of x:"))
    y = int(input("enter value of y:"))
    result = x / y
    print(x)
except:
    print("there is an error")
else:
    print("succesful division")

#finally

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



