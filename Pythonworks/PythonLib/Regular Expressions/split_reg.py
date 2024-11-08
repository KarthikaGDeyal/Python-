import re
mystring="Introduction to regular expression in python"
x=re.split("\s",mystring)
print(x)
print(type(x))
x=re.split("to",mystring)
print(x)