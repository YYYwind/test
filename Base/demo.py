#coding=utf-8
from selenium import webdriver
import unittest
import HTMLTestRunner
import sys
from time import sleep
import xlrd
reload(sys)
sys.setdefaultencoding("utf-8")
class baidutest:
    def __init__(self,path):
        self.path=path
    def load(self):
        #打开一个excel文件
        excel=xlrd.open_workbook(self.path)
        #获取一个工作表格
        table=excel.sheets()[0]
        #获取工作表格的行数
        nrows=table.nrows
        #循环遍历数据，将他存到list中去
        test_data=[]
        for i in range(1,nrows):
            print table.row_values(i)
            test_data.append(table.row_values(i))
        #返回数据列表
        return test_data
class baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url="http://www.baidu.com"
        self.path=u"aa.xlsx"

    def test_baidu_search(self):
        driver=self.driver
        print u"开始第一个用例百度搜索"
        #加载测试数据
        testinfo=baidutest(self.path)
        data=testinfo.load()
        print data
        #循环参数化
        for d in data:
            #打开百度首页
            driver.get(self.url)
            #验证标题
            self.assertEqual(driver.title,u"百度一下，你就知道")
            sleep(1)
            driver.find_element_by_id("kw").clear()
            #参数化搜索词
            driver.find_element_by_id("kw").send_keys(d[0])
            sleep(1)
            driver.find_element_by_id("su").click()
            sleep(1)
            print d[0]
            print driver.title
            print d[1]
            #验证搜索结果的标题
            self.assertEqual(driver.title,d[1])
            sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    test=unittest.TestSuite()
    test.addTest(baidu("test_baidu_search"))
    htmlpath=u"D:\\aaaaaaaa.html"
    fp=file(htmlpath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"baidu测试",description=u"测试用例结果")
    runner.run(test)
    fp.close()