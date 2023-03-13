import sys

print(str(sys.argv))

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv[5])
print(sys.argv[6])

dic={sys.argv[1]:sys.argv[2],sys.argv[3]:sys.argv[4],sys.argv[5]:sys.argv[6]}

print(dic)
if "name" in dic :
    del sys.argv[3]
print(dic)