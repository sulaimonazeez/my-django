import requests
import re
from bs4 import BeautifulSoup
x = requests.get('https://quotex.com')
soup = BeautifulSoup(x.content)

add = " \n"
result = soup.find_all('svg')
for data in result:
  y = data.find_all('path')
  for tar in y:
    print(tar.has_attr('d'))
    add += tar["d"]
with open("rename.txt", "w+") as file:
  file.write(add)
  print("done")
print(dir(data))