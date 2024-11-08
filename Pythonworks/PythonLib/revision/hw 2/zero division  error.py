try:
    num1=int(input("enter the value of num1:"))
    num2=int(input("enter the value of num2:"))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("error occurred")