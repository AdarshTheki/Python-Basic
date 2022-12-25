# Polymorphisam:

# Overloading: function name same but parameter change(same or change), 
# Overriding: Method having same name with the same arguments 

# l = [10,20,30,40]
# print(len(l))
# s = "Welcome"
# print(len(s))

class Ws:
    def displayinfo(self,name=''):
        print("Welcome the first programming", name)
        print("Welcome the second programming" + name)

obj = Ws()
obj.displayinfo()
obj.displayinfo('python') # function Overloading

class AA:
    def desplay(self):
        print("Welcome to AA")
class BB(AA):
    def desplay(self):
        super().desplay()  # Parent function call
        print("Welcome to BB")
obj = BB()
obj.desplay() # Function Overriding