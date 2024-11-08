import re
mystring="Introduction to regular expressions in pythom reg"
x=re.search("reg",mystring)
print(x)
print(x.start())
print(x.end())
x=re.search("luminar",mystring)
print(x)
x=re.search("\s",mystring)
print(x)