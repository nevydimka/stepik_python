a = int(input())
cache = {}
for i in range(a):
    x = int(input())
    if x in cache:
        print(*cache[x])
    else:
        cache.setdefault(x, []).append(f(x))
        print(*cache[x])