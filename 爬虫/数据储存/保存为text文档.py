import requests
from pyquery import PyQuery as pq
header={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}#请求头

url='https://blog.csdn.net/weixin_46211269/article/details/113728894'
page=requests.get(url=url,headers=header).content.decode('utf-8')
# print(page)
doc=pq(page)

#方法一
file=open('yuan.txt','w',encoding='utf-8')
file.write(page)
file.close()

#方法二(这种好一些)
with open('wen.txt','w',encoding='utf-8') as f:
    f.write(page)
