binary = []
bin  = [x for x in input().split(',')]
for p in bin:
    x = int(p, 2)
    if not x % 5:
        binary.append(p)
print(','.join(binary))