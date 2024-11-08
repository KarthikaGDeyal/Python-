class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def display(self):
        print("name:",self.name)
        print("course:",self.course)
obj=Student("Vipin","Python")
obj.display()