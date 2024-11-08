class Person:
    def __init__(self):
        self.name=""
        self.age=""
    def Person_details(self):
        self.name=input("enter your name:")
        self.age=int(input("enter your age:"))
    def display_person(self):
        print("name:",self.name)
        print("age:",self.age)
class Company:
    def __init__(self):
        self.companyname=""
        self.location=""
        self.contact=""
    def Company_details(self):
        self.companyname=input("enter company name:")
        self.location=input("enter location:")
        self.contact=int(input("enter contact no:"))
    def display_company(self):
        print("name:",self.companyname)
        print("location:",self.location)
        print("contact:",self.contact)
class Employee(Person,Company):
    def __init__(self):
        self.designation=""
        self.salary=""
        self.skill=""
        self.gender=""
    def Employee_details(self):
        self.designation=input("enter your designation:")
        self.salary=int(input("enter your salary:"))
        self.skill=input("enter your skill:")
        self.gender=input("enter your gender:")
    def display_employee(self):
        print("designation:",self.designation)
        print("salary:",self.salary)
        print("skill:",self.skill)
        print("gender:",self.gender)
obj=Employee()
obj.Person_details()
obj.Company_details()
obj.Employee_details()
obj.display_person()
obj.display_company()
obj.display_employee()
