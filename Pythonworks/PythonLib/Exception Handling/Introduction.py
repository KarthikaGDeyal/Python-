try:
    x=int(input("enter value of x:"))
    y=int(input("enter value of y:"))
    result=x/y
    print(result)

except ZeroDivisionError:
    print("error occurred")