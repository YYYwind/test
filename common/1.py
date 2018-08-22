from urllib import request,parse
import requests
import urllib
import http.cookiejar
url = 'http://w-beta-1000.chemanman.com:4901/api/Login/Login/login?gid=320'
dict = {
    'req': '{"group_id":"320","user_name":"CY","password":"202cb962ac59075b964b07152d234b70"}'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/68.0.3440.'
                  '84 Safari/53''7.36'
}
data = bytes(parse.urlencode(dict), encoding="utf-8")
f = request.Request
print(data)
req = request.Request(url=url, data=data, headers=headers, method="POST")
# response = request.urlopen(req)
# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
response = opener.open(req)
print(response.Cookie)
print(cj)
#print(response.read().decode("utf-8"))