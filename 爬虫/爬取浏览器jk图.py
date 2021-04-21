import requests
from lxml import etree
import time
from fake_useragent import UserAgent
url='https://cn.bing.com/images/search?q=jk%e5%a5%b3%e7%94%9f&qs=n&form=QBIR&sp=-1&pq=jk%e5%a5%b3%e7%94%9f&sc=0-4&cvid=61017D07691A4806B09ABB59FF96C8FF&first=1&tsc=ImageBasicHover'
headers = {'user-agent':UserAgent().random}
response=requests.get(url=url,headers=header)#发送请求
# print(response.text)
data=etree.HTML(response.text)#转化为html格式
image_url=data.xpath('//a//img[@class="mimg"]//@src')
print(image_url)
path='E://photo//'