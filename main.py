import re
from bs4 import BeautifulSoup

with open("index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, 'html.parser')

# title = soup.title.string
# print(title)

# .find() or find_all()

# page_h1_all = soup.find_all("h1")
# print(page_h1_all)
#
# for item in page_h1_all:
#     print(item.text)

# user_name = soup.find("div", class_="user__name")
# # user_name = soup.find("span")
# print(user_name.text.strip())

# user_name = soup.find("div", class_="user__name").find("span").text
# print(user_name)

# find_all_spans_in_users_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_users_info)

# for item in find_all_spans_in_users_info:
#     print(item.text)

# print(find_all_spans_in_users_info[0].text)
# print(find_all_spans_in_users_info[2].text)

# social_networks = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_networks)
# for item in social_networks:
#     name_sn = item.text
#     link_sn = item.get("href")
#     print(f"{name_sn}: {link_sn}")

# post_div = soup.find(class_="post__text").find_parent("div", "user__blog__wall")
# print(post_div)

# search parents up to user__post
# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)

next_elem = soup.find(class_="post__title").next_element.next_element.text
print(next_elem)

next_elem = soup.find(class_="post__title").find_next().text
print(next_elem)