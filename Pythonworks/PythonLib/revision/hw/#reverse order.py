a=[1,2,3,4]

print("orginal array:")
for i in range(len(a)):
    print(a[i],end= " ")


print("\nreversed array:")
for i in range(len(a)-1,-1,-1):
    print(a[i],end= " ")
