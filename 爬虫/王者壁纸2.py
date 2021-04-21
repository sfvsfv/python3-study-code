import requests
from urllib import parse
import os
from urllib import request


# 添加请求头U-A和referer,避免反爬
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'referer': 'https://pvp.qq.com/web201605/wallpaper.shtml'}

# 定义一个函数来获取每张图片的url
def extract_images(data):
    image_urls = []
    for x in range(1, 9):
        # 每组图片共8张,通过这种方式获取一组照片的所有地址
        # 通过.unquote解码地址,并且替代末尾的'200'为'0'
        image_url = parse.unquote(data['sProdImgNo_%d' % x]).replace('/200', '/0')
        image_urls.append(image_url)

    return image_urls

def page_url_list(base_url):

    page_urls = []
    for i in range(23):
        base_page_url = base_url.format(
            str(i))
        page_urls.append(base_page_url)

    # print(page_urls)
    return page_urls

def main():
    # 确认页面url地址
    base_url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1597489758464k'

    page_urls = page_url_list(base_url)

    for page_url in page_urls:

        resp = requests.get(page_url, headers=headers)

        result = resp.json()

        datas = result['List']

        for data in datas:
            # 通过图片地址处理函数处理列表数据
            image_urls = extract_images(data)

            # 获取图片的名称,由于要按照文件名创建目录,所以要对空格进行处理
            name = parse.unquote(data['sProdName']).strip()
            # print('-' * 70)
            # print(name)
            # print('-' * 70)
            # print(image_urls)
            # print('-' * 70)

            # 先创建一个用来存放image的主目录
            # 当文件夹不存在时创建,当存在时跳过
            if os.path.exists('./image') == False:
                os.mkdir('image')
            else:
                pass
            # 创建一个文件夹./image/name/
            # 创建路径
            dirpath = os.path.join('image',name)
            # 按照路径创建文件夹
            os.mkdir(dirpath)

            # 下载图片
            # 注意index索引值写前边
            for index,image_url in enumerate(image_urls):

                # request.urlretrieve(,)传参地址和路径,就可以保存图片
                # 每个图片的地址是不同的,按照保存路径,图片名称,和索引+1以及文件类型名称的路径保存
                request.urlretrieve(image_url,os.path.join(dirpath,name+'%d.jpg' % (index + 1)))
                print(name,'%s下载成功' % image_url)

if __name__ == '__main__':
    main()