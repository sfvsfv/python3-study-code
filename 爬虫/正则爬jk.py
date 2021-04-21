import requests
import re
import urllib.request
import time
import os
header={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}
url='https://cn.bing.com/images/async?q=jk%E5%88%B6%E6%9C%8D%E5%A5%B3%E7%94%9F%E5%A4%B4%E5%83%8F&first=118&count=35&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&SFX=4'
request=requests.get(url=url,headers=header)
c=request.text
pattern=re.compile(
    r'<div class="imgpt".*?<div class="img_cont hoff">.*?src="(.*?)".*?</div>',re.S
)
items = re.findall(pattern, c)
# print(items)
os.makedirs('E://photo/',exist_ok=True)
for a in items:
    print("下载图片："+a)
    b=a.split('/')[-1]
    urllib.request.urlretrieve(a,'E://photo/'+str(int(time.time()))+'.jpg')
    print(a+'.jpg')
    time.sleep(2)