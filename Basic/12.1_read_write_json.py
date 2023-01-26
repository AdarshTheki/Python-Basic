import json
d = '{"key":"value","name":"adarsh","age":45,"fees":8000}'
x = json.loads(d)
print(x)
for a in x:
    print(a,x[a])

# Read and Write json:
import json
file = open("post.json","r")
x = file.read()
finalfile = json.loads(x)

for a in finalfile:
    print(a['title'],a['userId'])
