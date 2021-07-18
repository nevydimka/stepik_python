import requests
with open('/home/user/Documents/Python/part3/dataset_4.txt') as data:
    lines = data.read().strip()
r = requests.get(lines)
with open('/home/user/Documents/Python/part3/output_4.txt', "a") as f:
    f.write(str(len(r.text.splitlines())))