

import requests

base = "https://stepic.org/media/attachments/course67/3.6.3/"
filename = "699991.txt"

url = base + filename

response = requests.get(url)
while not response.text.startswith("We"):
    filename = response.text
    url = base + filename

    response = requests.get(url)


print(response.text)
