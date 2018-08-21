import xlrd



data = xlrd.open_workbook('../file/1.xls')
table = data.sheets()[0]
print (data.sheet_names())
print (table.cell_value(1, 3))
#print tables.cell_value(2, 3)
"""
def load(self):
    # 打开一个excel文件
    excel = xlrd.open_workbook(self.path)
    # 获取一个工作表格
    table = excel.sheets()[0]
    # 获取工作表格的行数
    nrows = table.nrows
    # 循环遍历数据，将他存到list中去
    test_data = []
    for i in range(1, nrows):
        print
        table.row_values(i)
        test_data.append(table.row_values(i))
    # 返回数据列表
    return test_data

data = xlrd.open_workbook(filename='../file/1.xls')
load(data)
"""