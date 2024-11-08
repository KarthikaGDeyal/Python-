from datetime import date
def days(date1,date2):
    if date2 > date1:
        return (date2-date1).days
    else:
        return (date1-date2).days
date1=date(2012,12,13)
date2=date(2012,2,25)
print("no of days between 2 dates:",days(date1,date2))