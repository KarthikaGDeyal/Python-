import re
mystring="Introduction to regular expressions in python to"
x=re.findall("to",mystring)
print(x)
x=re.findall("regular",mystring)
print(x)
x=re.findall("luminar",mystring)
print(x)

#search
x=re.search("reg",mystring)
print(x)
x=re.search("expre",mystring)
print(x)
x=re.search("luminar",mystring)
print(x)
x=re.search("\s",mystring)
print(x)

#split
mystring="Introduction to regular expressions in python"
x=re.split("\s",mystring)
print(x)

x=re.split("to",mystring)
print(x)

#sub
mystring="Introduction to regular expressions in python"
x=re.sub("\s","_",mystring)
print(x)

x=re.sub("to","_",mystring)
print(x)