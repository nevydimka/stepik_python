a = input().lower().split()
d = {}
for i in a:
    d.setdefault(i, []).append(a.count(i))
for x in d:
    print(x, a.count(x))