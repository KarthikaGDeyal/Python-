class A:
     def function_A(self):
        print("inside class A")
class B(A):
    def function_B(self):
        print("Inside class B")
class C(B):
    def function_C(self):
        print("inside class C")
obj=C()
obj.function_A()
obj.function_B()
obj.function_C()