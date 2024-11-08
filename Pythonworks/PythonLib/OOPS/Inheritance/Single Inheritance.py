class College():
    def __init__(self):
        self.College_name=""
        self.Location=""
        self.Contact_no=""
    def college_details(self):
        self.College_name=input("enter the name of college:")
        self.Location=input("enter the location of college")
        self.Contact_no=int(input("enter the contact no:"))
    def display_college(self):
        print("College Name:",self.College_name)
        print("Location:",self.Location)
        print("Contact no:",self.Contact_no)
class Department(College):
    def __init__(self):
        self.Dept_ID=""
        self.Dept_Name=""
        self.HOD_Name=""
        self.Dept_Mobile=""
    def dept_details(self):
        self.Dept_ID=int(input("enter id:"))
        self.Dept_Name=input("enter dept name:")
        self.HOD_Name=input("enter HOD name:")
        self.Dept_Mobile=int(input("enter no:"))
    def display_dept(self):
        print("Dept_ID:",self.Dept_ID)
        print("Dept_Name:",self.Dept_Name)
        print("HOD_Name:",self.HOD_Name)
        print("Dept_Mobile:",self.Dept_Mobile)
obj1=Department()
obj1.college_details()
obj1.display_college()
obj1.dept_details()
obj1.display_dept()