# Dictionary:
d = {
    'key':'value',
    'name':'adarsh',
    'age':'45',
    'fees':8000
}
print(d)   # {'key': 'value', 'name': 'adarsh', 'age': '45', 'fees': 8000}
print(d.get('key')) # value

for n in d:
    print(d[n])  # value  #adarsh  #45  #8000

for n in d.keys():
    print(n)
print(d.keys())     # dict_keys(['key', 'name', 'age', 'fees'])

for n in d.values():
    print(n)
print(d.values())   # dict_values(['value', 'adarsh', '45', 8000])

for a,b in d.items():
    print(a,b)
print(d.items())    # dict_items([('key', 'value'), ('name', 'adarsh'), ('age', '45'), ('fees', 8000)])

# delete: (only used key)
del d['age']
print(d)    # {'key': 'value', 'name': 'adarsh', 'fees': 8000}

d.pop('fees')
print(d)    # {'key': 'value', 'name': 'adarsh'}

p = dict(nam='pay',fed=30) #create dictionary
print(p)    # {'nam': 'pay', 'fed': 30}

p.update({'fed':100})
print(p)

p['desc']='Enter value'
print(p)    # {'nam': 'pay', 'fed': 100, 'desc': 'Enter value'}

p.clear() # clear all
print(p)  # {}

# Nested Dictionary:
course = {
    'php':{'sub':'eng', 'fees':1500,'age':'ten'},
    'python':{'sub':'hindi', 'colg':100,'age':'two'},
    'java':{'sub':'marthi', 'blog':0,'age':10}
}
print(course['php'])  # {'sub': 'eng', 'fees': 1500, 'age': 'ten'}
print(course['php']['fees'])  # 1500
for k,v in course.items():
    print(k,v)