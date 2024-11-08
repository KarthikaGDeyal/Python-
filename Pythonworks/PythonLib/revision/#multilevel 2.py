class College:
    def __init__(self):
        self.collegename=""
        self.location=""
        self.contactno=""
    def details_College(self):
        self.collegename=input("enter college name:")
        self.location=input("enter location:")
        self.contactno=int(input("enter contact no:"))
    def display_College(self):
        print("name:",self.collegename)
        print("location:",self.location)
        print("contact no:",self.contactno)
class Department(College):
    def __init__(self):
        self.id=""
        self.hodname=""
        self.contact=""
        self.name=""
    def details_dept(self):
        self.id=int(input("enter id:"))
        self.hodname=input("enter hodname:")
        self.contact=int(input("enter contact no:"))
        self.deptname=input("enter  dept name:")
    def display_dept(self):
        print("id:",self.id)
        print("hodname:",self.hodname)
        print("contact:",self.contact)
        print(" dept name:",self.deptname)
class Student(Department):
    def __init__(self):
        self.studentname=""
        self.age=""
        self.email=""
        self.course=""
        self.place=""
        self.mobile=""
    def details_student(self):
        self.studentname=input("enter student name:")
        self.age=int(input("enter age:"))
        self.email=input("enter email:")
        self.course=input("enter course:")
        self.place=input("enter place:")
        self.mobile=int(input("enter contact no:"))
    def display_student(self):
        print("student name:",self.studentname)
        print("age:",self.age)
        print("email:",self.email)
        print("course:",self.course)
        print("place:",self.place)
        print("mobile:",self.mobile)
obj=Student()
obj.details_College()
obj.details_dept()
obj.details_student()
obj.display_College()
obj.display_dept()
obj.display_student()


















































