from urllib import request,parse
import xlrd
import json
import ast
import demjson

data = xlrd.open_workbook('../file/1.xls')
table = data.sheets()[0]


url = table.cell_value(1,0)
headers = table.cell_value(1,1)
name = table.cell_value(1,2)
value = json.loads(table.cell_value(1,3))
headers = json.loads(headers)

#body = '"' + name + '":"' + value + '"'
#body = name + ':' + value


#body = json.loads(body)

print(headers)


data = bytes(parse.urlencode(value), encoding="utf-8")
a= name+'='+data
print(a)
"""
print(type(data))

req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))
"""

#b'req=%7B%22group_id%22%3A%22320%22%2C%22user_name%22%3A%22CY%22%2C%22password%22%3A%22202cb962ac59075b964b07152d234b70%22%7D'