class democlass:
    def __init__(self):
        self.name=""
        self.place=""
    def data(self):
        self.name=input("enter name:")
        self.place=input("enter place:")
    def display(self):
        print("name:",self.name)
        print("place:",self.place)
obj=democlass()
obj.data()
obj.display()