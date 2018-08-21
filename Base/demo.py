import xlrd
def open_excel(file = 'file.xls'):#打开要解析的Excel文件
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)

def excel_by_index(file = 'file.xls', colindex = 0, by_index = 0):#按表的索引读取
    data = open_excel(file)#打开excel文件
    tab = data.sheets()[by_index]#选择excel里面的Sheet
    nrows = tab.nrows#行数
    ncols = tab.ncols#列数
    colName = tab.row_values(colindex)#第0行的值
    list = []#创建一个空列表
    for x in range(1, nrows):      #第一行为标题（第一行为0），所以从第二行开始
        row = tab.row_values(x)
        if row:
            app = {}#创建空字典
            for y in range(0, ncols):
                app[colName[y]] = row[y]
            list.append(app)
    return list

def test_user_management():
    listdata = excel_by_index('../file/1.xls')
    print(listdata[1])
