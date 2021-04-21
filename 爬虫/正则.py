#抓取网页
import requests
import re
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}
url='https://maoyan.com/board/4'
request = requests.get(url=url,headers=headers)
print(request.text)

c=request.text
# print(c)
pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
                   +'(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>'
                   +'(.*?) </i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
item=re.findall(pattern,c)
print(item)