n = int(input())
a = ''
b = ''
c = 0
d = 0
keyset = {}
total = {}
points = {}
win = {}
draw = {}
lose = {}
dataset = []
for i in range(n):
     dataset.append(input().split(';'))
for i in dataset:
    a = i[0]
    b = i[2]
    c = int(i[1])
    d = int(i[3])
    keyset.setdefault(a, [])
    keyset.setdefault(b, [])
    total.setdefault(a, [])
    total.setdefault(b, [])
    points.setdefault(a, [])
    points.setdefault(b, [])
    draw.setdefault(a, [])
    draw.setdefault(b, [])
    lose.setdefault(a, [])
    lose.setdefault(b, [])
    win.setdefault(a, [])
    win.setdefault(b, [])
    if c > d:
        win.setdefault(a, []).append(1)
        points.setdefault(a, []).append(3)
        lose.setdefault(b, []).append(1)
    elif d > c: 
        win.setdefault(b, []).append(1)
        points.setdefault(b, []).append(3)
        lose.setdefault(a, []).append(1)
    else:
        points.setdefault(a, []).append(1)
        points.setdefault(b, []).append(1)
        draw.setdefault(a, []).append(1)
        draw.setdefault(b, []).append(1)
    if a in total:
        total.setdefault(a, []).append(1)
    if b in total:
        total.setdefault(b, []).append(1)
total = dict([(key, sum(values)) for key, values in total.items()])
points = dict([(key, sum(values)) for key, values in points.items()])
win = dict([(key, sum(values)) for key, values in win.items()])
draw = dict([(key, sum(values)) for key, values in draw.items()])
lose = dict([(key, sum(values)) for key, values in lose.items()])
for i in keyset:
    print(i + ':' + str(total[i]), win[i], draw[i], lose[i], points[i])