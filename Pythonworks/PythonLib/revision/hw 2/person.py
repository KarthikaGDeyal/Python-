from datetime import datetime
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth= datetime.strptime(date_of_birth,"%Y-%m-%d")




    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
obj=Person("john","london","2001-01-6")
print(obj.calculate_age())