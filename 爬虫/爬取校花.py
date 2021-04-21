# 3.re爬取校花,图片,名称,点赞,评论
# https://www.duitang.com/search/?kw=%E6%A0%A1%E8%8A%B1&type=feed
import requests
import re
import xlwt
import urllib
import urllib.request
import logging
logging.captureWarnings(True)


def getHtml():
    url = "https://www.duitang.com/search/?kw=%E6%A0%A1%E8%8A%B1&type=feed"
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
        "Connection": 'Keep-Alive'}
    res = requests.get(url=url, headers=headers, verify=False)
    res.encoding = 'utf-8'
    html = res.text
    return html


def getcontent(html):
    rules = re.compile(
        r'<div class="j">.*?alt="(.*?)" data-iid="" src="(.*?)".*?<div class="d2 "><i></i><span>(.*?)</span></div>.*?<div class="d1 "><i></i><span>(.*?)</span></div>',
        re.S)
    content = re.findall(rules, html)
    return content


def saveDataToDatalist():

    html = getHtml()
    datalist = []
    for i in getcontent(html):
        data = []
        for k in range(0, 4):
            data.append(i[k])
        datalist.append(data)
    return datalist


def saveToexcel(path, datalist):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('校花', cell_overwrite_ok=True)
    col = ('名称', '图片', '赞', '收藏')
    for i in range(0, 4):
        # 第一个参数行,第二个参数列,第三个参数写入数据
        sheet.write(0, i, col[i])
    for i in range(0, len(datalist)):
        data = datalist[i]
        for j in range(0, 4):
            sheet.write(i + 1, j, data[j])
        book.save(path)


def savePic(datalist):
    for i in range(0, len(datalist)):
        url = datalist[i][1]

        # filename = ".校花/%d.jpg" % i
        filename='校花/%d.jpg'%i
        urllib.request.urlretrieve(url=url, filename=filename)

datalist = saveDataToDatalist()
saveToexcel("校花.xls", datalist)

savePic(datalist)
