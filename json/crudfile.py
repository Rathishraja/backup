import json


x = {
  "name": "John",
  "city": "Torronto"
}

u= {
    "name": "shiva",
    "city": "washington"
}


y = json.dumps(x)
v = json.dumps(u)

print(y)
print(v)