import re
from bs4 import BeautifulSoup

with open("index2.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, 'html.parser')

# title = soup.title.string
# print(title)

# .find() or .find_all()

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

# next_elem = soup.find(class_="post__title").next_element.next_element.text
# print(next_elem)
#
# next_elem = soup.find(class_="post__title").find_next().text
# print(next_elem)

# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)
#
# next_sib = soup.find(class_="post__title").find_previous_sibling()
# print(next_sib)

# next_sib = soup.find(class_="post__date").find_next_sibling().find_next().text
# print(next_sib)

# links = soup.find(class_="some__links").find_all("a")
# print(links)
#
# for item in links:
#     # link_href_atr = item.get("href")
#     link_href_atr = item["href"]
#     # link_data_atr = item.get("data-attr")
#     link_data_atr = item["data-attr"]
#     print(item.text)
#     print(link_href_atr)
#     print(link_data_atr)

# find_word = soup.find("a", text=re.compile("Одежда"))
# print(find_word)

# parsing one word through site
# find_word = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_word)

find_word = soup.find("tr").find("td").find("a").text
print(find_word)
# for item in find_word:
#     print(item)

