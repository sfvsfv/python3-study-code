import requests
from bs4 import BeautifulSoup
# from  fake_useragent import UserAgent

url='https://movie.douban.com/cinema/nowplaying/xian/'

# headers={
#     'User-Agent':UserAgent().random
# }
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

response=requests.get(url=url,headers=headers)

html=response.text
# print(html)
soup=BeautifulSoup(html,'lxml')
li_list=soup.find_all(name='li')
# print(li_list)
for li  in li_list:
    # print(li.findAll(name='a'))
    for a in li.findAll(name='a'):
        print(a.string)