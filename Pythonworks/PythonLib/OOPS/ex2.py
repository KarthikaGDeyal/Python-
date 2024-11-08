class Myclass:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("course:",self.course)

obj=Myclass("anu",21,"python")
obj.display()
obj1=Myclass("ria",23,"java")
obj1.display()
