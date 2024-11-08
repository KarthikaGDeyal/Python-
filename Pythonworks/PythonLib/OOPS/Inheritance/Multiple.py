class A:
    def function_A(self):
        print("Inside class A")
class B:
    def function_B(self):
        print("Inside class B")
class C(A,B):
    def function_C(self):
        print("Inside class C")
obj=C()
obj.function_A()
obj.function_B()
obj.function_C()