class College:
    def college_function(self):
        print("inside college class")
class Department(College):
    def department_function(self):
        print("inside department class")
obj=Department()
obj.department_function()
obj.college_function()