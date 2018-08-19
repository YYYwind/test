from urllib import request,parse

url = 'http://w-beta-1000.chemanman.com:4901/api/Login/Login/login?gid=320'
dict = {
    'req': '{"group_id":"320","user_name":"CY","password":"202cb962ac59075b964b07152d234b70"}'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/68.0.3440.'
                  '84 Safari/53''7.36'
}
data = bytes(parse.urlencode(dict), encoding="utf8")
req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))

