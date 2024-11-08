try:
    x=int(input("enter x:"))
    y=int(input("enter y:"))
    result=x/y
    print(result)

except ZeroDivisionError:
    print("error occured")