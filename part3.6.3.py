import requests
url = 'https://stepik.org/media/attachments/course67/3.6.3/'
d = ['We'] #last word
with open('/home/user/Documents/Python/part3/dataset_5.txt') as data:
    par = data.read().strip()
r = requests.get(par)
p = requests.get(par).text
k = p.splitlines()
while (k[0]) != (d[0]):
    r = requests.get(url + p)
    p = (requests.get(url + p).text)
    k = p.split(' ')
with open('/home/user/Documents/Python/part3/output_5.txt', "a") as f:
    f.write(p)