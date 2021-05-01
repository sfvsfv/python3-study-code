import requests
import re

# 设置保存路径
path = './girl'
# 目标url
url = "http://pic.netbian.com/4kmeinv/index.html"
# 伪装请求头  防止被反爬
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Referer": "http://pic.netbian.com/4kmeinv/index.html"
}

# 发送请求  获取响应
response = requests.get(url, headers=headers)
# 打印网页源代码来看  乱码   重新设置编码解决编码问题
# 内容正常显示  便于之后提取数据
response.encoding = 'GBK'

# 正则匹配提取想要的数据  得到图片链接和名称
img_info = re.findall('img src="(.*?)" alt="(.*?)" /', response.text)

for src, name in img_info:
    img_url = 'http://pic.netbian.com' + src   # 加上 'http://pic.netbian.com'才是真正的图片url
    img_content = requests.get(img_url, headers=headers).content
    img_name = name + '.jpg'
    with open(path + img_name, 'wb') as f:     # 图片保存到本地
        print(f"正在为您下载图片：{img_name}")
        f.write(img_content)
