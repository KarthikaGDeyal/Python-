class employee:
    def __init__(self,name,place,email,mobile,course,company):
        self.name=name
        self.place=place
        self.email=email
        self.mobile=mobile
        self.course=course
        self.company=company
    def display_data(self):
        print("name:",self.name)
        print("place:",self.place)
        