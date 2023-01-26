# Python in Oops:- Creating Classes

class Employee:
    def __init__(self, first, last, pay):  # constructor
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last +'@company.com'
    
    def fullname(self):  # instance method
        return '{} {}'.format(self.first, self.last)

# create objects
emp_1 = Employee('adarsh','verma',50000)
emp_2 = Employee('ayush','Verma', 30000)

# Call

print(emp_1)            # <__main__.Employee object at 0x00000138790bbfa0>
print(emp_1.email)      # adarsh.verma@company.com

emp_1.fullname()        

print(emp_1.fullname())             # adarsh verma
print(Employee.fullname(emp_1))     # adarsh verma
print(emp_2.fullname())             # ayush Verma