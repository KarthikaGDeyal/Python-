class Person:
    def __init__(self):
        self.name=""
        self.age=""
    def details_person(self):
        self.name=input("enter name:")
        self.age=int(input("enter age:"))
    def display_person(self):
        print("name:",self.name)
        print("age:",self.age)
class Company:
    def __init__(self):
        self.companyname=""
        self.location=""
        self.contact=""
    def details_company(self):
        self.companyname=input("enter company name:")
        self.location=input("enter location:")
        self.contact=int(input("enter contact no:"))
    def display_company(self):
        print("name:",self.companyname)
        print("location:",self.location)
        print("contact no;",self.contact)
class Employee(Person,Company):
    def __init__(self):
        self.designation=""
        self.salary=""
        self.skill=""
        self.gender=""
    def details_employee(self):
        self.designation=input("enter designation:")
        self.salary=int(input("enter salary"))
        self.skill=input("enter skills:")
        self.gender=input("enter gender:")
    def display_employee(self):
        print("designation:",self.designation)
        print("salary:",self.salary)
        print("skill:",self.skill)
        print("gender:",self.gender)
obj=Employee()
obj.details_person()
obj.details_company()
obj.details_employee()
obj.display_person()
obj.display_company()
obj.display_employee()