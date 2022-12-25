# String:

s = 'Welcome to home'
print(type(s))      #  <class 'str'>
print(s[5])         #  m
# indexcing slicing string
print(s[5:14])      #  me to hom
print(s[:5])        #  Welco
print(s[5:])        #  me to home
print(s[0::2])      #  Wloet oe
print(s[-1::-2])    #  eo teolW
# iteration in string
t = len(s)
print(t)            # 15
for a in range(t):
    print(s[a])     # W e l c o m e  t..

# In-build function in string
m = s.upper()   # upper case string
n = s.lower()   # lower case string
o = s.title()   # every first words capital 
p = s.capitalize()  # only first word capital
q = s.find('to')    # 
r = s.index()       #       
u = s.isalpha()     # all char then True otherwise False
v = s.isdigit()     # all no. then true otherwise False
w = s.isalnum()     # all char and no. True otherwise False( @, *, % )
x = chr(65)         # convert integer 65 to ASCII ('A')
print(type(x), x)   # <class 'str'> A
y = ord('A')        # Convert ASCII ('A') to 'int' 65

# String Formate:
txt = "welcome to {b} {a} how".formate(b="Adarsh",a=10)
print(txt)  # welcome to Adarsh 10 how

txt1 = "welcome to {b:10} {a} how".formate(b="Adarsh",a=10)
print(txt1)     # welcome to     adarsh 10 how
