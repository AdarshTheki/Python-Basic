# Inheritance
class A:   
    def display_A(self):
        print("welcome to Wacode A")

class B(A):  # Single Inheritance
    def display_B(self):
        print("welcome to Wacode B")

class C(B):  # Multi-levl Inheritance
    def display_C(self):
        print("welcome to Wacode C")

class D: 
    def display_D(self,):
        print("welcome to Wacode D")

class E(A,D): # Multiple Inheritance
    def display_E(self):
        print("welcome to Wacode E")

obj = B()
obj.display_A()
obj.display_B()

obj = C()
obj.display_A()
obj.display_B()
obj.display_C()

obj = E()
obj.display_A()
obj.display_D()
obj.display_E()