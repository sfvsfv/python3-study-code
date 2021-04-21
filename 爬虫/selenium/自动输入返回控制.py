# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# driver.find_element_by_id("kw").clear()#清楚输入框原来的内容
# driver.find_element_by_id("kw").send_keys("selenium")#找到输入框，输入selenium
# driver.find_element_by_id("su").click()#找到‘百度一下’，点击进行搜索
#
# driver.quit()


from selenium import webdriver
from time import sleep
import numpy as np
random = np.random.RandomState(0)#RandomState生成随机数种子
a = random.uniform(36.1,36.5)#随机数范围
c=round(a,1)#精度设置为1个小数点

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

search_text = driver.find_element_by_id('kw')#找到输入框
search_text.send_keys('%s'%c)#输入内容
# search_text.submit()#submit相当于回车，跟click差不多
# sleep(5)#5秒后关闭
# driver.quit()


# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# # 获得输入框的尺寸
# size = driver.find_element_by_id('kw').size
# print(size)
#
# # 返回百度页面底部备案信息
# text = driver.find_element_by_class_name('s-bottom-layer-content').text#备案信息为文本
# print(text)
#
# # 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
# attribute = driver.find_element_by_id("kw").get_attribute('type')
# print(attribute)
# #
# # # 返回元素的结果是否可见， 返回结果为 True 或 False
# result = driver.find_element_by_id("kw").is_displayed()
# print(result)
#
# driver.quit()
