from bs4 import BeautifulSoup  # BeautifulSoup是用来解析HTML的内容的
import requests

content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser")
all_prices = soup.findAll("p", attrs={"class": "price_color"})
# 找出所有书本的价格并以字符串形式输出，“p”是结果所在标签，attrs是为了根据属性筛选符合条件的元素，
for price in all_prices:
    print(price, price.string[2:])  # string字符串可以获得HTML包围的内容
all_titles = soup.findAll("h3")
for title in all_titles:
    links = title.find("a")
    for link in links:
        print(link.string)
print(soup.p)
print(soup)