operator=input("enter the operator(+,-,*,/):")
a=(int(input("enter the value of a:")))
b=(int(input("enter the value of b:")))
if operator == "+":
    result=(a+b)
    print(result)
elif operator == "-":
    result=(a-b)
    print(result)
elif operator == "*":
    result=(a*b)
    print(result)
elif operator == "/":
    result=(a/b)
    print(result)
else:
    print("operator not valid")
