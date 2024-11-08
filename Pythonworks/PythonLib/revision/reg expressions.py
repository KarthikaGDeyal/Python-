import re
mystring="introduction to regular expressions in python to"
x=re.findall("to",mystring)
print(x)
x=re.findall("luminar",mystring)
print(x)
x=re.search("reg",mystring)
print(x)
print(x.start())
print(x.end())
x=re.split("to",mystring)
print(x)
x=re.sub("to","_",mystring)
print(x)
x=re.split("to",mystring)
print(x)

