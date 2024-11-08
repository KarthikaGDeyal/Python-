class College:
    def __init__(self):
        self.collegename=""
        self.location=""
        self.contactno=""
    def college_details(self):
        self.collegename=input("enter college name:")
        self.location=input("enter location:")
        self.contactno=input("enter contact no:")
    def display_college(self):
        print("college name:",self.collegename)
        print("location:",self.location)
        print("contactno:",self.contactno)
class Department(College):
    def __init__(self):
        self.dept_id=""
        self.hodname=""
        self.dept_contact=""
        self.deptname=""
    def department_details(self):
        self.dept_id=int(input("enter id:"))
        self.hodname=input("enter hod name:")
        self.dept_contact=int(input("enter contact:"))
        self.deptname=input("enter dept name:")
    def display_dept(self):
        print("dept_id:",self.dept_id)
        print("hodname:",self.hodname)
        print("dept_contact:",self.dept_contact)
        print("deptname:",self.deptname)

class Student(Department):
    def __init__(self):
        self.name=""
        self.age=""
        self.email=""
        self.course=""
        self.place=""
        self.mobile=""
    def studentdetails(self):
        self.name=input("enter name:")
        self.age=int(input("enter age:"))
        self.email=input("enter email:")
        self.course=input("enter course:")
        self.place=input("enter place")
        self.mobile=int(input("enter mobile:"))
    def display_student(self):
        print("name:",self.name)
        print("age:",self.age)
        print("email:",self.email)
        print("course:",self.course)
        print("place:",self.place)
        print("mobile:",self.mobile)
obj1=Student()
obj1.college_details()
obj1.display_college()
obj1.department_details()
obj1.display_dept()
obj1.studentdetails()
obj1.display_student()