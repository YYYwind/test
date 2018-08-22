from urllib import request,parse
import xlrd
import requests

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
send = requests.Session()
#data = bytes(parse.urlencode(data), encoding="utf-8")  # Request 方法中data格式必须是字节流
req = send.post(url=url, data=data, headers=headers)  # 发送请求
print(type(data))
print(req.text)

def result():  # 定义断言
    if ":0," in req.text:
        print('测试通过')
    else:
        print('测试失败')

if __name__ == '__main__':
    result()
    print('响应状态：',req.status_code)

