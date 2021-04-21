import requests#发送请求
from lxml import etree#处理数据
header={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}#请求头

url='https://ibaotu.com/shipin/7-0-0-0-0-1.html'#网址

response=requests.get(url=url,headers=header)#发送请求

html_text=response.content.decode('utf-8')#编译

html=etree.HTML(html_text)#自动修正html文档

video_url=html.xpath('//div[@class="video-play"]/video/@src')#视频网址

video_names=html.xpath('//span[@class="video-title"]/text()')#视频名称
# print(video_url,video_names)
path='D://code//my python code//爬虫//shipin//'#视频存放地址
for src,title in zip(video_url,video_names):
    video_url = "https:" + src#视频url
    url=video_url.replace(".mp4_10s","")#增加画质url
    file_name = (title + ".mp4")#文件名
    response=requests.get(url=url,headers=header)#在此发送新的请求
    with open(path+file_name,'wb') as f:    #把文件写入path地址
        f.write(response.content)
        print("%s下载成功"%file_name)

# for i in range(1,3):
#     print(f"正在爬取第{i}页:")
#     url = 'https://ibaotu.com/shipin/7-0-0-0-0-' + str(i) + '.html'
#     response = requests.get(url=url, headers=header)  # 在此发送新的请求
#     html_text = response.content.decode('utf-8')  # 编译
#     html = etree.HTML(html_text)  # 自动修正html文档
#     video_url = html.xpath('//div[@class="video-play"]/video/@src')  # 视频网址
#     video_names = html.xpath('//span[@class="video-title"]/text()')  # 视频名称
#     for src, title in zip(video_url, video_names):
#         video_url = "https:" + src  # 视频url
#         url = video_url.replace(".mp4_10s", "")  # 增加画质url
#         file_name = (title + ".mp4")  # 文件名
#         # print(file_name)
#         response = requests.get(url=url, headers=header)  # 在此发送新的请求
#         # print(response.content)
#         with open(path+file_name,'wb') as f:
#             f.write(response.content)
#             print("%s下载成功" % file_name)
