import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'

r = requests.get(url)

inf = open('https://stepic.org/media/attachments/course67/3.6.3/' + 'r')

with open('https://stepic.org/media/attachments/course67/3.6.3/') as inf:
    s1 = inf.readline()
    s2 = inf.readline()


print(r.text.splitlines())