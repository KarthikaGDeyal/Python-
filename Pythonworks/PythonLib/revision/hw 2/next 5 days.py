import datetime
today=datetime.date.today()
for x in range(0,5):
    print(today+datetime.timedelta(days=x))
