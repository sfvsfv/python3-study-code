
from selenium import webdriver
#1.引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
driver = webdriver.Chrome(executable_path ="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver")

driver.get("https://www.baidu.com")
driver.maximize_window()
#2.定位到要悬停的元素
element= driver.find_element_by_id('s-usersetting-top')

#3.对定位到的元素执行鼠标悬停操作
# ActionChains(driver).move_to_element(element).perform()
element.click()
#找到链接
elem1=driver.find_element_by_link_text("搜索设置")
elem1.click()

#通过元素选择器找到id=sh_2,并点击设置
elem2=driver.find_element_by_id("sh_1")
elem2.click()

#保存设置
elem3=driver.find_element_by_class_name("prefpanelgo")
elem3.click()

# perform()： 执行所有 ActionChains 中存储的行为；
#
# context_click()： 右击；
#
# double_click()： 双击；
#
# drag_and_drop()： 拖动；
#
# move_to_element()： 鼠标悬停。
