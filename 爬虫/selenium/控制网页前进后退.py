from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver')

#访问百度首页
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)#获取当前百度网页

#访问新闻页面
second_url='https://www.taobao.com'
print("now access %s" %(second_url))
driver.get(second_url)#获取当前新闻网页

#返回（后退）到百度首页
print("back to  %s "%(first_url))
driver.back()

#前进到新闻页
print("forward to  %s"%(second_url))
driver.forward()

driver.refresh() #刷新当前页面

driver.quit()#退出