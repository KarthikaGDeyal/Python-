class Student:
    def __init__(self,name,age,place,mobile,course):
        self.name=name
        self.age=age
        self.place=place
        self.mobile=mobile
        self.course=course

    def display_data(self):
        print("name:",self.name)
        print("age:",self.age)
        print("place:",self.place)
        print("mobile:",self.mobile)
        print("course:",self.course)

obj1=Student("anu",21,"cochin",23456718,"python")
obj1.display_data()
obj2=Student(age="24",place="london",course="java",mobile=90876543,name="ria")
obj2.display_data()