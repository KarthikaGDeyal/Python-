class Calculator:
    def addition(self,x,y):
        return x+y

    def subtraction(self,x,y):
        return x-y

    def multiplication(self,x,y):
        return x*y

    def division(self,x,y):
        return x/y
obj=Calculator()
print(obj.addition(3,5))
print(obj.subtraction(13,5))
print(obj.multiplication(3,5))
print(obj.division(30,5))
