class College:
    def __init__(self):
        self.collegename=""
        self.location=""
        self.contactno=""
    def details_college(self):
        self.collegename=input("enter college name:")
        self.location=input("enter college location:")
        self.contactno=input("enter contact no:")
    def display_college(self):
        print("collegename:",self.collegename)
        print("location:",self.location)
        print("contact no:",self.contactno)
class Department(College):
    def __init__(self):
        self.dept_id=""
        self.deptname=""
        self.hodname=""
        self.deptcontact=""
    def details_dept(self):
        self.dept_id=int(input("enter dept id:"))
        self.deptname=input("enter deptname:")
        self.hodname=input("enter hodname:")
        self.deptcontact=input("enter deptcontact:")
    def display_dept(self):
        print("dept id:",self.dept_id)
        print("deptname:",self.deptname)
        print("hodname:",self.hodname)
        print("deptcontact:",self.deptcontact)
obj=Department()
obj.details_college()
obj.details_dept()
obj.display_college()
obj.display_dept()