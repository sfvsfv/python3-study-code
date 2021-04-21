import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq
headers={
    'UserAgent':UserAgent().random
}

url='https://kengdie.com/'#搞笑网网址

html = requests.get(url=url,headers=headers).content.decode('utf-8')

doc=pq(html)#初始化html字符串

img=doc('.card-bg img')#获取card-bg下内容的img标签

path='D://code//my python code//爬虫//image//'
for item in img.items():
    # print(item.attr('data-src'))
    title=item.attr('alt')#获取标题
    title=title+'.gif'
    src=item.attr('data-src')#获取照片地址
    src1=src.replace('mw200','large')
    src2=src1.replace('thumb150','large')

    response=requests.get(url=src2,headers=headers)
    with open(path+title,'wb') as f:
        f.write(response.content)
        print('下载成功:%s'%title)
