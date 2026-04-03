"""
HTTP: Hypertext Transfer Protocol 超文本传输协议


HTTP请求（客户端至服务器）
1. get方法：获得数据
2. post方法：创建数据
Example
请求行：POST /user/info HTTP/1.1 (POST方法类型，/user/info资源路径，HTTP/1.1协议版本)
请求头：Host:www.example.com (Host指主机域名，主机域名结合请求行里的资源路径，可以得到一个完整的网址)
      User-Agent:curl/7.77.0 (curl命令行工具发出请求的User-Agent)
      Accept；*/* (Accept是在告诉服务器，客户端想要接收的响应数据是什么类型的)
                  1. 接收HTML，text/html
                  2. 接收JSON，application/json
                  3. 接收HTML与JSON，text/html,application/json
                  4. 接受任意类型，*/*
请求体：{"username": "小马", "email": "2780"} (请求体里可以放客户端传给服务器的其他任意数据，get方法的请求体里一般是空的)


HTTP相应（服务器至客户端）
状态行：HTTP/1.1 200 OK (HTTP/1.1协议版本，200状态码，OK状态消息)
       常见状态码和状态消息：200 OK（客户端请求成功）
                         301 Moved Permanently（资源被永久移动到新地址）
                         400 Bad Request（客户端无法被服务器所理解）
                         401 Unauthorized（请求未经授权）
                         403 Forbidden（服务器拒绝提供服务）
                         404 Not Found（请求资源不存在）
                         500 Internal Server Error（服务器发生不可预期的错误）
                         503 Server Unavailable（服务器当前不能处理客户端的请求）
响应头: Date: Fri, 27 Jan 2023 02:10:48 GMT
       Content-Type: text/html; charset=utf-8 (响应类型是HTML，编码是UTF-8)
响应体: <!DOCTYPE html>
         <head><title>首页</title></head>
         <body><h1>小马<h1><p>哈喽! </p></body>
       </html> (服务器想给客户端的数据内容)
"""
import requests
# 把爬虫程序伪装成正常的浏览器，如果没有这一行会被服务器拒绝（例如418：418表示服务器已经知道了你是在爬虫，不会回复你）
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get("http://books.toscrape.com/")
print(response)  # 是一个response的实例，代表着服务器发回给我们的响应（<Response[200]>）
print(response.status_code)   # 正常的状态码为200
if response.ok:
    print(response.text)
else:
    print("请求失败！")
