import json

f = open("newfile.json","w")




dic = {
    "name": "rathish",
    "class": "a",
    "dep": "IT"
}

json.dump(dic,f)

print("new file is created")