# Function, How works are ! :

def first_fun():
    print("Hello World-1")
print(first_fun())
first_fun()
# Hello World-1
# None
# Hello World-1

# Function Return Value:(not print value)
def seconf_fun():
    return "My World is best!-2"
print("Hey", seconf_fun())
print(seconf_fun().upper())  
seconf_fun()
# Hey My World is best!-2
# MY WORLD IS BEST!-2

# Function Argument with Perameter value:
def third_fun(greeting, name='You'):
    return "{},{}".format(greeting,name)
print(third_fun("Hi"))
print(third_fun("Hi", name="Adarsh"))
# Hi,You
# Hi,Adarsh

def forth_fun(*a, **b):
    print("a: ",a)
    print("b: ",b)

forth_fun("math","arts",name="Adarsh",age=22)
# a:  ('math', 'arts')
# b:  {'name': 'Adarsh', 'age': 22}

course = ['Math','Arts']
info = {'name':'Jone','age':24}

forth_fun(course, info)
# a:  (['Math', 'Arts'], {'name': 'Jone', 'age': 24})
# b:  {}

forth_fun(*course,**info)
# a:  ('Math', 'Arts')
# b:  {'name': 'Jone', 'age': 24}