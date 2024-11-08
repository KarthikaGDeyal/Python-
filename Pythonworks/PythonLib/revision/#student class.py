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


obj=Student("anu",21,"cochin",34876789,"python")
obj.display_data()
