import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.233.400 QQBrowser/12.3.5574.400"
}  # 任意网页右键“检查”，network中任意name的header的User-Agent
response = requests.get("http://movie.douban.com/top250", headers=headers)  # URL为网址，headers作为传入get方法里面headers这个可选参数的值
print(response)
print(response.status_code)
print(response.text)
