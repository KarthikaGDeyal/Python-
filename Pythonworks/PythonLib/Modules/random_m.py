import random

print(random.randint(1000,10000))
x=["python","java","html",1,2,3,4,5,6,7,8,9]
print(x)
random.shuffle(x)
print(x)

y=["python","java","html",1,2,3,4,5,6,7,8,9]
print(random.choice(y))
