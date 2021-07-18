text = open("dataset_2.txt", 'r')
s = text.read().replace('\n', ' ').upper().split()
text.close()
d = []
b = 0
for i in s:
    if (s.count(i)) > b:
        d.clear()
        d.append(i)
        b = s.count(i)
    else:
        continue
with open("output_2.txt", "a") as f:
    for item in d:
        f.write(str(item) + ' ' + str(b))