import random


#random
x=["abc","def","ghi","jkl"]
random.shuffle(x)
print(x)
y=["abcde",1,2,3,4]
print(random.choice(y))

#datetime
import datetime
z=datetime.datetime.now()
print(z)
print(z.year)
print(z.month)
print(z.day)
print(z.hour)
print(z.minute)
print(z.second)

#strftime
import datetime
x=datetime.datetime.now()
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%d"))
print(x.strftime("%D"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%b"))
print(x.strftime("%B"))

#calendar
import calendar
print(calendar.month(2024,12))
print(calendar.calendar(2024))