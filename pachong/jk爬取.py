''
'https://cn.bing.com/images/async?q=jk%e5%88%b6%e6%9c%8d%e5%a5%b3%e7%94%9f%e5%a4%b4%e5%83%8f&first=42&count=35&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*0_y*0_h*0_c*5_i*36_r*6&IG=9BB720932F484381A6E28F2ECA3791C6&SFX=2&iid=images.5530'
f'https://cn.bing.com/images/async?q=jk%e5%88%b6%e6%9c%8d%e5%a5%b3%e7%94%9f%e5%a4%b4%e5%83%8f&first={81}&count=35&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*0_y*0_h*0_c*5_i*{71}_r*{12}&IG=9BB720932F484381A6E28F2ECA3791C6&SFX={3}&iid=images.5530'
'https://cn.bing.com/images/async?q=jk%e5%88%b6%e6%9c%8d%e5%a5%b3%e7%94%9f%e5%a4%b4%e5%83%8f&first=117&count=35&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*0_y*0_h*0_c*5_i*106_r*18&IG=9BB720932F484381A6E28F2ECA3791C6&SFX=4&iid=images.5530'
'https://cn.bing.com/images/async?q=jk%e5%88%b6%e6%9c%8d%e5%a5%b3%e7%94%9f%e5%a4%b4%e5%83%8f&first=154&count=35&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*788_y*972_h*185_c*4_i*141_r*24&IG=C6F1D0A3A441449FB175AE6FDAA716D3&SFX=5&iid=images.5530'
'https://cn.bing.com/images/async?q=jk%e5%88%b6%e6%9c%8d%e5%a5%b3%e7%94%9f%e5%a4%b4%e5%83%8f&first=195&count=35&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*398_y*982_h*187_c*2_i*176_r*30&IG=C6F1D0A3A441449FB175AE6FDAA716D3&SFX=6&iid=images.5530'
'https://cn.bing.com/images/async?q=jk%e5%88%b6%e6%9c%8d%e5%a5%b3%e7%94%9f%e5%a4%b4%e5%83%8f&first=233&count=35&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*202_y*1005_h*190_c*1_i*211_r*36&IG=C6F1D0A3A441449FB175AE6FDAA716D3&SFX=7&iid=images.5530'

'https://cn.bing.com/images/async?q=jk%e5%88%b6%e6%9c%8d%e5%a5%b3%e7%94%9f%e5%a4%b4%e5%83%8f&first=557&count=12&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*413_y*994_h*190_c*2_i*526_r*89&IG=C6F1D0A3A441449FB175AE6FDAA716D3&SFX=16&iid=images.5530'
import requests, re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0'
                  '; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/70.'
                  '0.3538.25 Safari/537.36 Core/1.'
                  '70.3732.400 QQBrowser/10.5.3819.400'
}

def url_reques(url):
    return requests.get(url, headers=headers).text


def img_reques(url):
    return requests.get(url, headers=headers).content


def main():
    for i in range(1, 17):
        print(f'正在爬取第{i}页')
        for img_url in re.findall(r'<div class="imgpt".*?<div class="img_cont hoff">.*?src="(.*?)".*?</div>', url_reques(f'https://cn.bing.com/images/async?q=jk%e5%88%b6%e6%9c%8d%e5%a5%b3%e7%94%9f%e5%a4%b4%e5%83%8f&first={4 + 37 * i}&count=35&relp=35&cw=1177&ch=705&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*0_y*0_h*0_c*5_i*{1 + 35 * i}_r*{6 * i}&IG=9BB720932F484381A6E28F2ECA3791C6&SFX={i}&iid=images.5530')):
            with open('./image/' + img_url[38:64] + '.jpg', 'wb') as f:
                f.write(img_reques(img_url))


if __name__ == '__main__':
    main()
