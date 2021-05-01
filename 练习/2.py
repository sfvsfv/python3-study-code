# #！/usr/bin/python
# # - * - coding:UTF-8 - * -
# import calendar
# cal = calendar.month(2016,1)
# print("以下输出2016年1月份的日历")
#
# print(cal)

# import numpy as np
# b=np.array([[1,2,3],[4,5,6]])
# # print(b)
# c=b.ravel()
# print(c)

# httpx.AsyncClient() as client:
import requests,re,json
from jsonpath import jsonpath
# url = 'https://api.66mz8.com/api/iciba.php?format=json'
# resp = requests.get(url)
# data = resp.json()
#
# note = data.get('note')
# content = data.get('content')
#
# print(note,content)
# def ji():

# url = 'https://api.66mz8.com/api/weather.php?location=上海'
# resp = requests.get(url,timeout=5)
# data=resp.json()
# day=data['data'][0]['days']
# week=data['data'][0]['week']
# wendu=data['data'][0]['temperature']
# weather=data['data'][0]['weather']
# wind=data['data'][0]['wind']
# pic = data['data'][0]['weather_icon']
# print(data)
# ji()

# coding=utf-8
# import time
# d=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(d)
# import requests,re
# ur='http://www.crys.top/api/kwdg.php?msg=逆战&n=1&c=text'
# d=requests.get(url=ur).text
# print(d)
# tu = re.findall('图片：(.*)', d)
# print(tu)
# ur = re.findall('链接：(.*)', d)[0]
# print(ur)

# import math as m
# a=int(input())
# b=int(input())
# c=int(input())
# a,b,c=map(int,input().split('\t'))
#
# p=(a+b+c)/2
# print(p)
# if a+b>c and a+c>b and b+c>a:
#     C=a+b+c
#     print("周长:%.2f" %(C))
#     S=m.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("面积：%.2f" %(S))
# else:
#     print("不能构成三角形")

# import requests
# from bs4 import BeautifulSoup
# url = 'https://music.163.com/artist?id=3684'
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.4071 SLBChan/30'}
# resp = requests.get(url,headers=headers)
# soup = BeautifulSoup(resp.text, 'html.parser')
# inf = soup.find('ul',class_='f-hide')
# information = inf.find_all('a')
# number = 0
# path='D://code//my python code//爬虫//shipin//'
# for i in information:
#     number=number+1
#     name=i.text
#     newname=name+'.mp3'
#     web=i.get('href')
#     url='https://music.163.com/song/media/outer/url?'+web
#     url = url.replace('/song?', '')
#     response = requests.get(url=url, headers=headers)  # 在此发送新的请求
#     # print(name)
#     print(url)
#     with open(path+newname,'wb') as f:
#         f.write(response.content)
#         print("%s下载成功" % newname)

# import requests
# import os
#
# if __name__ == '__main__':
#     # 确认目标的url
#     url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/MTI5MDc0OTc=/18536cce20942eea8a6642c6e4ffe94b/ec6ce3ee6cfbeb31295104ebb3e25d1d.mp4?wsSecret=b968a857db5318e0ae73e2e3cfa6ab90&wsTime=1618245127'
#     # 构造请求头参数
#     headers = {
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
#         'Referer':'https://music.163.com/'
#     }
#     # 发送请求，获取响应
#     response = requests.get(url,headers=headers)
#     # 数据为字节类型
#     bytes_data = response.content
#     # 保存数据
#     with open('那些你很冒险的梦.mp4','wb')as f:
#         f.write(bytes_data)
#     # 将MV中的纯视频分离出来
#     os.system('ffmpeg -i "那些你很冒险的梦.mp4" -vn -y -acodec copy 那些你很冒险的梦.m4a')
#     # 将原来的mv删除
#     os.remove('那些你很冒险的梦.mp4')

