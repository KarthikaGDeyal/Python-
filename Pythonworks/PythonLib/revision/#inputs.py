class democlass:
    def __init__(self):
        self.name=""
        self.place=""
    def student_data(self):
        self.name=input("enter your name:")
        self.place=input("enter your place:")
    def display_data(self):
        print("name:",self.name)
        print("place:",self.place)
obj=democlass()
obj.student_data()
obj.display_data()