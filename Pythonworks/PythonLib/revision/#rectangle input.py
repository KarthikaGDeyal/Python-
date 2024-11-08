class Area:
    def __init__(self):
        self.length=""
        self.breadth=""
    def data(self):
        self.length=int(input("enter length:"))
        self.breadth=int(input("enter breadth:"))
    def display(self):
        print("area:",self.length * self.breadth)

obj=Area()
obj.data()
obj.display()