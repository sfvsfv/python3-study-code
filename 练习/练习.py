# import urllib3
#
# http=urllib3.PoolManager()
#
# url='https://movie.douban.com/chart'
#
# headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#            'Connection':'keep-alive',
#            'Accept-Encoding':''}
#
# # tm=urllib3.Timeout(connect=1.0,read=3.0)
#
# # rq=http.request('GET',url,retries=5,rediect=4)
#
# rq=http.request('GET',url,headers=headers)
#
# print('服务器响应码：',rq.status)
#
# print('获取内容为：',rq.data.decode('utf-8'))



 # import requests

# url='https://movie.douban.com/chart'
#
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


# rq=requests.get(url,headers=headers)

# print('状态码：',rq.status_code)
# print('编码：',rq.encoding)
# print('结果类型：',type(rq))
# print('响应头：',rq.headers)
# print(rq.text)

#正则匹配
# import re

# ac=re.compile(r'\d+')
#
# print('成功匹配出：',re.findall(ac,'udvwiu64816wddw6351'))

# ac=re.compile((r'\d+'))#转换用于匹配的正则表达式
#
# print('成功匹配：',re.search(ac,'ewuf557ww55'))
#
# import re
# import requests
# import chardet
#
# url='https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D0%A3%BB%A8&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#            'Connection':'keep-alive',
#            'Accept-Encoding':'',
#            'Cookie': 'pgv_info=ssid=s7806817766; ts_last=www.qq.com/; pgv_pvid=406447215; ts_uid=999821371; pac_uid=0_5f2629c454e66; ad_play_index=73; fp3_id1=1100DE9BC0059F0D4FD0661E28145889ED7A731C2419E0C6FB21773062E8C29A83A91AB4A4D720B9E8EF375309B05029FC67'
# }
# rq=requests.get(url,headers=headers)
#
# rq.encoding=chardet.detect(rq.content)['encoding']
#
#
# title_pattern=r'(?<=<title>).*?(?=</title>)'
# title_com=re.compile(title_pattern,re.M|re.S)
# title_search=re.search(title_com,rq.text)ii
#
# title=title_search.group()

# print('标题内容为：',title)
# print(rq)
#
# print('标题内容为：',re.findall(r'<title>(.*?)</title>'

# import matplotlib.pylab as plt
# squers=[1,5,6,8,12]
# plt.plot(squers)
# plt.show()
#
# import matplotlib.pyplot as pyt
# squers=[1,4,8,16,32,64]
#
# pyt.plot(squers,linewidth=5)
# #设置标题，坐标轴标签
# pyt.title("Squers numbers",fontsize=24)
# pyt.xlabel("Value",fontsize=24)
# pyt.ylabel("squers of value",fontsize=14)
#
# #设置刻度标记
# pyt.tick_params(axis="both",labelsize=14)
#
# pyt.show()
#折线图
# import matplotlib.pyplot as pyt
# input_values=[1,2,3,4,5]
# squers=[1,4,9,16,25]
# pyt.plot(input_values,squers,linewidth=5)
#
# pyt.title("Squers numbers",fontsize=24)
# pyt.xlabel("Value",fontsize=24)
# pyt.ylabel("squers of value",fontsize=14)
#
# #设置刻度标记
# pyt.tick_params(axis="both",labelsize=14)
#
# pyt.show()

#散点图
# import matplotlib.pyplot as plt
#
# x_values=[1,4,8,16]
# y_values=[1,4,16,64]
# plt.scatter(x_values,y_values,s=100)
#
# plt.title("squers number",fontsize=24)
# plt.xlabel("values",fontsize=24)
# plt.ylabel("squers of numbers",fontsize=14)
#
# plt.tick_params(axis="both",labelsize=14)
#
# plt.show()

# import matplotlib.pyplot as plt
#
# x_values=list(range(1,1001))
# y_values=[x**2 for x in x_values]
#
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors='none',s=40)#打大写首字母后面加个s
#
# plt.title("squers number",fontsize=24)
# plt.xlabel("values",fontsize=24)
# plt.ylabel("squers of numbers",fontsize=14)
#
# plt.tick_params(axis="both",labelsize=14)
#
# plt.axis([0,1001,0,1100000])
#
# # plt.show()
# plt.savefig('squers_plot.png',bbox_inches='
#encoding:utf-8

#
# setA = eval(input('请输入一个集合：'))
# setB = eval(input('再输入一个集合：'))
# print('交集：', setA & setB)
# print(' 并 集 ：', setA | setB)

# num = input('请输入一个自然数：')
# print(sum(map(int, num)))
#
# num = int(input('请输入一个自然数：'))
# print('二进制：', bin(num))
# print('八进制：', oct(num))
# print('十六进制：', hex(num))



2
