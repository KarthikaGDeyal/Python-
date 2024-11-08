class Area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth



    def display_data(self):
        print("length:",self.length)
        print("breadth:",self.breadth)
        print("area:",self.length * self.breadth)

obj=Area(5,2)
obj.display_data()