from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.233.400 QQBrowser/12.3.5574.400"
}
response = requests.get("http://movie.douban.com/top250", headers=headers).text
soup = BeautifulSoup(response, "html.parser")
all_titles = soup.findAll("span", attrs={"class": "title"})
# 含原版标题
for title in all_titles:
    print(title.string)
# 不含原版标题
for title in all_titles:
    if "/" not in title.string:
        print(title.string)

# 但是以上的都只是网页第一页的前25名的电影，接下来能够包含250个
# 通过观察网页的地址
for start_num in range(0, 250, 25):
    response = requests.get(f"http://movie.douban.com/top250?start={start_num}", headers=headers).text
    soup = BeautifulSoup(response, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        if "/" not in title.string:
            print(title.string)





