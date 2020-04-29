a = dict()
mass = input().split()
for i in mass:
    if i in a.keys():
        a[i] = a.get(i) + 1
    else:
        a[i] = 1
for i in a.keys():
    print(i, a[i])
