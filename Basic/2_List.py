# List: 
# Mutable(change), define list in  l = [1,2,3,..]

i = [ 1,2,3,[4,5,6] ] # indexing = print(i[3][1]) = 5
j = [ 2,3,"hello",[4,5,6]]  # indexing = print(j[2]) = hello

# List iteration :
t = len(i)
for a in range(t):
    print(i[a])

for a in i:
    print(a)

for a in range(t-1,-1,-1):
    print("last",i[a])

# List Comprehension:
l = []
for a in range(1,100):
    l.append(a)
print(l)
n = [m for m in range(1,100)]
print(n)
n = [m for m in range(1,100) if m%2==0]
print(n)

# List In-Build-Functon:
l = [20,30,40,50]
del l[2]        # remove 2 index value
l.pop(2)        # remove 2 index value
l.remove(60)    # remove 60 not index
l.clear()       # clear all
l.insert(0,10)  # 0 index value 10
l.append(70)    # last append same copy past
l.extend()      # last append value copy past
l.count()
l.sort()
l.reverse()
l.index()
x = max(l)
x = min(l)

# Zip-function in String
l1 = [10,20,30,40]
l2 = [3,4,5,6,80]
for a,b in zip(l1,l2):
    print(a,b)    # print a=b=4 indexing print

# Input Print in list:
a = input("enter the text: ")   # input = Enter the value of A
print(a)                        # Enter the value of A    
l = a.split()
print(l)                        # ['Enter', 'the', 'value', 'of', 'A']

m = []
for a in range(1,4):
    n=input("enter the value"+str(a)+" :-")
    m.append(n)     # input append 1 to 3
print(m)            # red green orange (input)

