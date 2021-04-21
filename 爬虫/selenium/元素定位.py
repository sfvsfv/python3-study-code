from selenium import webdriver#导入模块
browser=webdriver.Chrome()#初始化
browser.get('https://www.taobao.com')#get请求淘宝网页
#print(browser.page_source)#打印网页源码
href=browser.find_element_by_link_text('男装')#文本获取链接
# print(href)
lei=browser.find_element_by_class_name('service-bd')#class name定位
# print(lei)
id=browser.find_element_by_id('tb-beacon-aplus')#id定位
# print(id)
name=browser.find_elements_by_name('goods')#name定位
# print(name)
print("设置浏览器宽480、高800显示")
browser.set_window_size(480, 800)
browser.quit()#关闭浏览器
#类似还有：tag name，partial link text，xpath，css selector
# browser.close()#关闭浏览器


# from selenium import webdriver
#
# from time import sleep
# #1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
# browser = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver')
#
# #2.通过浏览器向服务器发送URL请求
# browser.get("https://www.baidu.com/")
#
# sleep(3)
#
# #3.刷新浏览器
# browser.refresh()
#
# #4.设置浏览器的大小
# browser.set_window_size(1400,800)
#
# #5.设置链接内容
# element=browser.find_element_by_link_text("新闻")
# element.click()
#
# element=browser.find_element_by_link_text("“下团组”时间")
# element.click()

