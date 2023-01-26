# Mathods and Constructors
class Democlass:
    a=10
    def showvalue(self):    # method
        # print(a)..... error
        self.c = self.a * self.a
        print(self.c)

    def showvalue1(self):   # method
        print("Welcome to Wscode")
    
    def showvalue2(self,a,b):  # Argument
        print(a+b)

    def __init__(self):     # constructor define and automatic call
        print("Constructor used automatic")

obj=Democlass()
obj.showvalue()
obj.showvalue1()
obj.showvalue2(20,30)