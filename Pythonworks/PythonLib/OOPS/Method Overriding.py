class Birds:
    def function1(self):
        print("there are multi[ple type of birds")
    def flight1(self):
        print("many of these birds can fly but some cannot")
class Sparrow(Birds):
    def flight1(self):
        print("Sparrows are the birds which can fly")
class Ostrich(Birds):
    def flight1(self):
        print("Ostriches are the birds which cannot fly")
obj1=Birds()
obj1.flight1()

obj2=Sparrow()
obj2.flight1()

obj3=Ostrich()
obj3.flight1()