"""
cj = http.cookiejar.CookieJar() #创建一个cookie对象，不传递参数说明创建了一个空的cookie对象
pro = urllib.request.HTTPCookieProcessor(cj) #创建一个cookie管理对象，来管理cj
opener = urllib.request.build_opener(pro) #用pro对象初始化一个opener，
"""