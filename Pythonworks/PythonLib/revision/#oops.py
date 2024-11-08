class myclass:
    name="nia"
obj=myclass()
print(obj.name)

class myclass():
    def student(self):
        print("name:anu")
obj=myclass()
obj.student()

class myclass():
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("course:",self.course)

obj=myclass("aiba",21,"python")
obj.display()
