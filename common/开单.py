import requests
import common
import xlrd

data = xlrd.open_workbook('../file/1.xls')
table = data.sheets()[0]
url = table.cell_value(2, 0)

name = table.cell_value(2, 2)
value = table.cell_value(2, 3)
data = {
    name: value
}

req1 =