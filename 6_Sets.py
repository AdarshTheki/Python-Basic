# Sets: Sets are Un-order and Un-index(unique value store)
# define: {}

s = {10,20,30,40}
set()
print('set',s)

s.add(50)
print('add',s)

s.pop()
print('pop',s)

s.remove(30)
print('remove',s)

s.discard(50)
print('discard',s)

s.clear()
print('clear',s)

l = [10,20,30,40,50]
s.update(l)
print('update',s)

# Summery:
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