with open('dataset_3.txt') as data:
    lines = data.read().splitlines()
lst = []
sum1st = 0
sum2st = 0
sum3st = 0
n = 0
output = []
for i in lines:
    lst.append(i.split(';'))
for el in lst:
    sumStud = ((int(el[1]) + int(el[2]) + int(el[3])) / 3)
    output.append(sumStud)
    output.append('\n')
    sum1st += (int(el[1]))
    sum2st += (int(el[2]))
    sum3st += (int(el[3]))
    n += 1
sum1st = sum1st / n
sum2st = sum2st / n
sum3st = sum3st / n
output.append(sum1st)
output.append(sum2st)
output.append(sum3st)
with open("output_3.txt", "a") as f:
    for item in output:
        f.write(str(item) + ' ')