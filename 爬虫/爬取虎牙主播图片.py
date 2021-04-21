import requests
from lxml import etree
import time
url='https://www.huya.com/g/4079/'
header={
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}
response=requests.get(url=url,headers=header)#发送请求
# print(response.text)
data=etree.HTML(response.text)#转化为html格式
image_url=data.xpath('//a//img//@data-original')
image_name=data.xpath('//a//img[@class="pic"]//@alt')
# print(image_url)
path='E://photo//'
for ur,name in zip(image_url,image_name):
    url=ur.replace('?imageview/4/0/w/338/h/190/blur/1','')
    title=name+'.jpg'
    response = requests.get(url=url, headers=header)  # 在此发送新的请求
    with open(path+title,'wb') as f:
        f.write(response.content)
    print("下载成功" + name)
    time.sleep(2)
