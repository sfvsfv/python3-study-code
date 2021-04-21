# import requests#发送请求
# from fake_useragent import UserAgent
# import os
# from lxml import etree
#
# headers={
#     'UserAgent':UserAgent().random
# }
#
# # os.mkdir("./王者壁纸/")
# path='./王者壁纸'
# url='http://pvp.qq.com/web201605/wallpaper.shtml###'
# response=requests.get(url=url,headers=headers)
# data=etree.HTML(response.content.decode('gbk'))#转化为html格式
# # print(data)
# z_url = data.xpath('//div[@id="Work_List_Container_267733"]//')
# print(z_url)
import requests
from urllib import parse
import os
import re
from urllib import request
page_num = 22
for page in range(page_num):
    url = r'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=%d&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1607857792418'%page
    hesders = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36','referer': 'https://pvp.qq.com/'}
    resp = requests.get(url=url,headers=hesders)
    result = resp.json()# 可以通过.json()直接处理,替代json.loads()将json字符串转化为字典
    datas = result["List"]  #通过字典的键取出对应的值
    for data in datas:
        wallpaper_url = parse.unquote(data['sProdImgNo_6']).replace('/200','/0') #sProdImgNo_6对应的是1920*1080分辨率的链接/200是缩略图/0才是正常图片
        wallpaper_name = re.sub(r':','比',parse.unquote(data['sProdName']))
        if os.path.exists('./王者荣耀1080P高清壁纸') == False:  # # 当文件夹不存在时创建,当存在时跳过
            os.mkdir('王者荣耀1080P高清壁纸')
        else:
            pass
        request.urlretrieve(wallpaper_url, os.path.join('./王者荣耀1080P高清壁纸', wallpaper_name+'.jpg'))
    print("第%d页爬取完成!!"%(page+1))
print('全部壁纸爬取完成!!')
