# Encapsulation: getter(), setter()

class Student:
    def __init__(self):
        self.__name = ""
    def getname(self):
        return self.__name
    def setname(self, name):
        self.__name = name

obj = Student()
obj.setname("testing")

givenname = obj.getname()
print(givenname)

#-----------------------------------

class Student_1:
    __name = "Ravi"
    def __init__(self):
        print(self.__name)
        self.__displayinfo() # print

    def __displayinfo(self):
        print("Hello World ! My names is 'Adarsh'")

obj = Student_1()
# print(obj.__name)