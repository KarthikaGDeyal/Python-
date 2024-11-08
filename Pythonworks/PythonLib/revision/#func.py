def MyFunction():
    print("introduction to python functions")
MyFunction()

def New_Function(Name):
    print("Hello",Name)
New_Function("Ashika")

#required arguments
def myfunction(name,age,place):
    print("*** WELCOME ***")
    print("name:",name)
    print("age:",age)
    print("place:",place)

myfunction("nia",23,"cochin")

#keyword arguments
def myfunction(name,age,place):
    print("name:",name)
    print("age:",age)
    print("place:",place)
myfunction(place="cochin",age=21,name="ria")


#default arguments
def default_arg(name,age=12):
    print("name:",name)
    print("age:",age)
default_arg("hari",22)
default_arg("haritha")


#variable length arguments
def student(name,course,*skills):
    print("name:",name)
    print("course:",course)
    print("skills:",skills)
student("ria","python","html","css")

#return
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
print("sum=",addition(12,3))
print("difference=",subtraction(12,3))


hi all