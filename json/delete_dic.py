import json


x = {
  "name": "kevin",
  "city": "montreal"
}

u= {
    "name": "shiva",
    "city": "washington"
}


y = json.dumps(x)
v = json.dumps(u)

print(y)
print(v)

if "name" in x :
    del x['name']
if "city" in x :
    del x['city']
print(x)
print(u)



