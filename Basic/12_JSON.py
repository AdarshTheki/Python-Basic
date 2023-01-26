# JSON: JavaScript Object Notation
# Important for API:

# JSON Formate: '{ }'
# p = '{"name":"Ws","lang":["python":"java"]}'

#       Converting Python Object to JSON:
# blog = {'URL':'www.google.com', 'name'='Wscode'}
# to_json = json.dump(blog)

import json
d = {
    'key':'value',
    'name':'adarsh',
    'age':'45',
    'fees':8000
}
f = json.dumps(d)
print(type(f))
print(f)
