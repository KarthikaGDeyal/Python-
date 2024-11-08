class A:
    def function_A(self):
        print("Inside parent class A")
class B(A):
    def function_B(self):
        print("Inside child class B")
class C(A):
    def function_C(self):
        print("Inside child class C")
class D(A):
    def function_D(self):
        print("Inside child class D")

obj1=B()
obj1.function_A()
obj1.function_B()

obj1=C()
obj1.function_A()
obj1.function_C()


obj1=D()
obj1.function_A()
obj1.function_D()