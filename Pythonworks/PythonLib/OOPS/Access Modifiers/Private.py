class Newclass:
    def __init__(self,name,place,course):
        self.__name=name
        self.__place=place
        self.__course=course
    def __display(self):
        print("name:",self.__name)
        print("place:",self.__place)
        print("course:",self.__course)
    def Access_private_function(self):
        self.__display()
obj=Newclass("Aryan","Kakkanad","Python")
obj.Access_private_function()