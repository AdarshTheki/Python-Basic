class Democlass:
    a=10

    def sumvalue(self):
        print(20+30)

demoobject = Democlass()
demoobject1 = Democlass()
print(demoobject.a)
print(demoobject1.a)
demoobject1.sumvalue()

# Creating Class and Object in Python

class Employee:
     # Class variables
    company_name = 'ABC Company'

    # constructor to initialize the object
    def __init__(self,name, salary):
        # instance varibles
        self.name = name
        self.salary = salary

    #instance method
    def show(self):
        print('Employee:- ', self.name, self.salary, self.company_name)

# Create First object 
emp2 = Employee('Adarsh',190000)
emp2.show()
# Create Second object 
emp2 = Employee('Emma',10000)
emp2.show()      