class Circle:
    def __init__(self,radius):
        self.radius=radius


    def display(self):
        print("radius:",self.radius)


    def area(self):
        print("area=",3.4*self.radius**2)

    def perimeter(self):
        print("perimeter=",2*3.14*self.radius)
obj=Circle(2)
obj.display()
obj.area()
obj.perimeter()