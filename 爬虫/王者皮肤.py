# import requests
# from lxml import etree
# from fake_useragent import UserAgent
# headers={
#     'User-Agent':UserAgent().random
# }
# url='http://pvp.qq.com/web201605/herolist.shtml'
# response=requests.get(url=url,headers=headers)#发送请求
# data=etree.HTML(response.text)#转化为html格式
# # print(data)
# z_url=data.xpath('//ul[@class="herolist clearfix"]//li//a//@href')
# # print(z_url)
# for n in z_url:
#     # print(n)
#     url1='http://pvp.qq.com/web201605/'+n
#     # print(url1)
#     new_response=requests.get(url=url1,headers=headers)
#     new_data=etree.HTML(new_response.text)
#     # print(new_data)
#     url2=new_data.xpath('//ul[@class=""pic-pf-list pic-pf-list3]')
#     print(url2)
# -*- coding: UTF-8 -*-
import requests
import os
import json
from lxml import etree
from fake_useragent import UserAgent
import logging

# 日志输出的基本配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


class glory_of_king(object):
    def __init__(self):
        if not os.path.exists("./王者荣耀皮肤"):
            os.mkdir("王者荣耀皮肤")
        # 利用fake_useragent产生随机UserAgent  防止被反爬
        ua = UserAgent(verify_ssl=False, path='fake_useragent.json')
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random
            }

    def scrape_skin(self):
        # 发送请求   获取响应
        response = requests.get('https://pvp.qq.com/web201605/js/herolist.json', headers=self.headers)
        # str转为json
        data = json.loads(response.text)
        # for循环遍历data获取需要的字段  创建对应英雄名称的文件夹
        for i in data:
            hero_number = i['ename']    # 获取英雄名字编号
            hero_name = i['cname']      # 获取英雄名字
            os.mkdir("./王者荣耀皮肤/{}".format(hero_name))  # 创建英雄名称对应的文件夹
            response_src = requests.get("https://pvp.qq.com/web201605/herodetail/{}.shtml".format(hero_number),
                                        headers=self.headers)
            hero_content = response_src.content.decode('gbk')  # 返回相应的html页面 解码为gbk
            # xpath解析对象  提取每个英雄的皮肤名字
            hero_data = etree.HTML(hero_content)
            hero_img = hero_data.xpath('//div[@class="pic-pf"]/ul/@data-imgname')
            # 去掉每个皮肤名字中间的分隔符
            hero_src = hero_img[0].split('|')
            logging.info(hero_src)
            # 遍历英雄src处理图片名称。
            for j in range(len(hero_src)):
                # 去掉皮肤名字的&符号
                index_ = hero_src[j].find("&")
                skin_name = hero_src[j][:index_]
                # 请求下载图片
                response_skin = requests.get(
                    "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg".format(
                        hero_number, hero_number, j + 1))
                # 获取图片二进制数据
                skin_img = response_skin.content
                # 把皮肤图片保存到对应名字的文件里
                with open("./王者荣耀皮肤/{}/{}.jpg".format(hero_name, skin_name), "wb")as f:
                    f.write(skin_img)
                    logging.info(f"{skin_name}.jpg 下载成功！！")

    def run(self):
        self.scrape_skin()


if __name__ == '__main__':
    spider = glory_of_king()
    spider.run()
