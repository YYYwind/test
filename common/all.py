import xlrd,requests,json

data = xlrd.open_workbook('../file/1.xls')
table = data.sheets()[0]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/68.0.3440.'
                  '84 Safari/53''7.36'
}
send = requests.Session()

def payloads(a,b):  #body体
    name = table.cell_value(a,b)
    c = b+1
    value = table.cell_value(a,c)
    data = {
        name: value
    }
    print(type(data))
    return data
def login():  #登录
    url = table.cell_value(1, 0)
    req = send.post(url=url,data=payloads(1, 2),headers=headers)  # 发送请求
    print(req.request.body)
    print(req.text)
    return req
def creat():
    url = table.cell_value(2, 0)
    req = send.post(url=url,data=payloads(2, 2),headers=headers)
    print(req.request.body)
    print(req.text)
    return req
"""
def result(a):  # 定义断言
    if ":0," in a:
        print('测试通过')
        print(login().text)
    else:
        print('测试失败')
        print(login().text)
    return 0
"""



if __name__ == '__main__':
    login()
    creat()
#    result(login())
#    print('响应状态：',login().status_code)

