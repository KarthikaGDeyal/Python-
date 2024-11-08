class Student:
    def __init__(self,rollno,name,age):
        self._rollno=rollno
        self._name=name
        self._age=age
    def _display(self):
        print("rollno:",self._rollno)
        print("age:",self._age)
class Newclass(Student):
    
    
    
    
    
    def __init__(self,name,rollno,age):
        Student.__init__(self,rollno,name,age)
    def display_data(self):
        print("name:",self._name)
        self._display()
obj=Newclass("Abinav",21,24)
obj.display_data()
