s=input("enter the string")
d = l = 0
for c in s :
    if(c.isdigit()):
        d=d+1
    elif(c.isalpha()):
        l=l+1
    else:
        pass
print("letter",l)
print("digit",d)