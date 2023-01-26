# List, Tuples, sets and Distionary
list = [1,2,3,4]
tup = (1,2,3,4)      # Not Change value
sets = {1,2,3,4}
dic = { 'key_1':'value',
      'key_2':'value',
      'key_3':'value',
      'key_4':'value',
    }
print(list,type(list))
print(tup,type(tup))
print(sets,type(sets))
print(dic,type(dic),"\n")
#--------------------------------

# Function, How works are ! :

def first_fun():
    print("Hello World-1")
print(first_fun())
first_fun()
#--------------------------------
def seconf_fun():
    return "My World is best!-2"
print("Hey", seconf_fun())
print(seconf_fun().upper())  
seconf_fun()
#---------------------------------
def third_fun(greeting, name='You'):
    return "{},{}".format(greeting,name)
print(third_fun("Hi"))
print(third_fun("Hi", name="Adarsh"))
#-----------------------------------
def forth_fun(*a, **b):
    print("a: ",a)
    print("b: ",b)

print("\n1st: ")
forth_fun("math","arts",name="Adarsh",age=22)

course = ['Math','Arts']
info = {'name':'Jone','age':24}

print("\n2nd: ")
forth_fun(course, info)

print("\n3rd: ")
forth_fun(*course,**info)