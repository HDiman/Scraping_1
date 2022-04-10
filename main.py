import re
from bs4 import BeautifulSoup

with open("index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, 'html.parser')

# title = soup.title.string
# print(title)

# .find() or find_all()

page_h1_all = soup.find_all("h1")
print(page_h1_all)

for item in page_h1_all:
    print(item.text)

