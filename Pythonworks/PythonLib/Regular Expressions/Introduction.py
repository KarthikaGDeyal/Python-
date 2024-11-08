import re
mystring="Introduction to regular expressions in python to"
x=re.findall("to",mystring)
x=re.findall("pre",mystring)
print(x)
print(len(x))