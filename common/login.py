from urllib import request,parse
import xlrd

data = xlrd.open_workbook('../file/1.xls')
table = data.sheets()[0]
url = table.cell_value(1, 0)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/68.0.3440.'
                  '84 Safari/53''7.36'
}
name = table.cell_value(1, 2)
value = table.cell_value(1, 3)
data = {
    name: value
}

data = bytes(parse.urlencode(data), encoding="utf-8")  # Request 方法中data格式必须是字节流
req = request.Request(url=url, data=data, headers=headers, method="POST")  # 发送请求
response = request.urlopen(req)  # 返回请求
res = response.read().decode("utf-8")  # 解析返回json


def result():  # 定义断言
    if ":0," in res:
        print('测试通过')
    else:
        print('测试失败')
# print(response.read().decode("utf-8"))


if __name__ == '__main__':
    result()
    print(res)
    print(req.headers['Cookie'])

