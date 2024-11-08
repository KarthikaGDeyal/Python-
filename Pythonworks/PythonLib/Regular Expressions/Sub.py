import re
mystring="Introduction to regular expressions in python"
x=re.sub("\s","_",mystring)
print(x)
x=re.sub("to","_",mystring)
print(x)