x=[1,2,80,50]
print(len(x))
min=x[0]
for i in range(len(x)):
    if x[i]<min:
        min=x[i]
print(min)