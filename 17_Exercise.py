class Area:
    def area_rect(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")
obj1 = Area()
obj1.area_rect()
obj1.area_rect(10)
obj1.area_rect(10,20) # Function Overloading

class A:
    def showdata(self):
        print("I am in 'A' class")
class B(A):
    def showdata(self):
        print("I am in 'B' class")
obj = B()
obj.showdata()  #  Function OverRiding