import re
from bs4 import BeautifulSoup

with open("index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, 'html.parser')

title = soup.title.string
print(title)
