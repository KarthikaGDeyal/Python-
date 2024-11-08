str1=("Python")
str2="Programming"
result=str1+str2
print(result)

#join
str1="Luminar"
str2="Technolab"
str3=" ".join([str1,str2])
str4="_".join([str1,str2])
print(str3)
print(str4)

#%
str1="Luminar"
str2="Technolab"
str3="Hello"
print("%s %s %s" %(str1,str2,str3))
print("%s_%s_%s" %(str1,str2,str3))

#format
str1="Luminar"
str2="Technolab"
print("{}{}".format(str1,str2))
print("{}_{}".format(str1,str2))

#comma
str1=input("enter first string:")
str2=input("enter second string:")
print(str1,str2)

#str function
x=123
print(type(x))
mystring=str(x)
print(type(mystring))