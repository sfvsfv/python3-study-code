import requests#请求模块
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
# }
headers={
    'User-Agent':UserAgent().random
}
url = 'https://www.shicimingju.com/book/hongloumeng.html'
page_text = requests.get(url=url,headers=headers).content.decode('utf-8')
soup= BeautifulSoup(page_text,'lxml')


mulu=soup.find_all(attrs={'class':'book-mulu'})
# mulu=soup.select('.book-mulu')
# print(mulu)
fp = open('./红楼梦.txt','w',encoding='utf-8')
for ul in mulu:
    a=ul.find_all(name='a')
    # print(a)
    for i in a:
        title = i.string
        new_url = 'https://www.shicimingju.com' + i['href']
        # print(new_url)
        # print(title)
        html=requests.get(url=new_url,headers=headers).content.decode('utf-8')
        new_soup=BeautifulSoup(html,'lxml')
        # print(soup)
        for  wenben in new_soup.find_all('div',{'class':'chapter_content'}):
            # print(wenben.text)
            c=wenben.text
            fp.write(title + ':' + c + '\n')
            print('下载成功%s!'%title)