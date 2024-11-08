class area:
    def __init__(self):
        self.length=""
        self.breadth=""
    def data(self):
        self.length=int(input("enter the length"))
        self.breadth=int(input("enter the breadth"))
    def display(self):
        print("length:",self.length)
        print("breadth:",self.breadth)
        print("area:",self.length*self.breadth)
x=area()
x.data()
x.display()

y=area()
y.data()
y.display()