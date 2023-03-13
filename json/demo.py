import json


x ={
 "users" : [
 {
 "name" : "John",
 "city" : "Toronto"
 },
 {
 "name" : "Shiva",
 "city" : "Washington"
 },
 {
 "name" : "Kevin",
 "city" : "Montreal"
 }
 ]
 }


y = json.dumps(x)

print(y)
if "Shiva" in y:
    del x['Shiva']
print(x)
