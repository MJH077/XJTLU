from bs4 import BeautifulSoup
import requests
headers = {
    "Usr-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.233.400 QQBrowser/12.3.5574.400"
}
response = requests.get("http://www.xjtlu.edu.cn", headers=headers).text
soup = BeautifulSoup(response, "html.parser")
all_title = soup.findAll("html")
print(all_title)

