inf = open('dataset.txt', 'r')  # open('file.txt')
s = inf.readline().strip()
inf.close()
a = ['0','1','2','3','4','5','6','7','8','9']
b = ""
c = 0
d = ''
e = ''
for i in s:
    if i not in a:
        if (b != ""):
            e = int(e)
            d += ((b) * e)
        b = i
        e = ''
    else:
        if type(e) == str:
            e += i
        else:
            e.append(i)
e = int(e)
d += (b * e)
ouf = open('output.txt', 'w')
ouf.write(d)
ouf.close()