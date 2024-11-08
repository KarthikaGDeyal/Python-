print(4*(6+5))
print(4*6+5)
print(4+(6*5))

#find square root of a no
a=int(input("enter a no:"))
print("square root is",a**0.5)

#square
a=int(input("enter a no:"))
print("square is",a**2)

#
a="hello"
print(a[1])

#reverse
a="hello"
print(a[::-1])

#oo
a="hello"
print(a[4])
print(a[-1])

#
a=[0]
print(a*3)
b=[0,0,0]
print(b)

#
list1=[1,2,[3,4,'hello']]
list1[2][2]='goodbye'
print(list1)

#
list2=[5,3,4,6,1]
list2.sort()
print(list2)

#
a="say sorry whenever you are does maps wrong"
for word in a.split():
    if word[0]=='s':
        print(word)

#
for i in range(0,11,2):
    print(i)

#
a=[x for x in range(1,51) if x%3==0]
print(a)

#
str="print every word in this sentence that has an even number of letters"
for i in str.split():
    if (len(i))%2==0:
        print(i)

#

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

#
str="create a list of the first letters of every word in this string"
a=[x[0] for x in str.split()]
print(a)