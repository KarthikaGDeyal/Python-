class A:
    def function_A(self):
        print("inside class A")
class B(A):
    def function_B(self):
        print("inside class B")
class C(B):
    def function_C(self):
        print("inside class C")
obj1=C()
obj1.function_A()
obj1.function_B()
obj1.function_C()