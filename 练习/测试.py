# import numpy as np
# arr = np.array([1, 5.5, 3, 15, 20])
# print(arr)
# print(arr.ndim)
# print(arr.shape)
# print(arr.dtype)

# import numpy as np
# import tensorflow as tf
# arr = np.array([1, 5.5, 3, 15, 20])
# tensor = tf.convert_to_tensor(arr,tf.float64)
# print(tensor)
#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'hyh'
# __date__ = '2020/11/8 13:00'

import requests, time, hashlib, urllib.request, re, json
from multiprocessing import Pool
import os, sys, threading
from tqdm import tqdm
import eventlet#导入eventlet这个模块
eventlet.monkey_patch()#必须加这条代码



maxconnections = 3
semlock = threading.BoundedSemaphore(maxconnections)
sys.setrecursionlimit(100000)
# 弹出保存视频路径
if (sys.platform.startswith('win')):
    # 如果是windows系统弹出
    import easygui

    path = easygui.diropenbox('视频保存路径: ')
else:
    path = input('请输入保存路径: ')


def get_play_list(start_url, cid, quality=80):
    """
    start_url = https://api.bilibili.com/x/web-interface/view?bvid + BV="/?p=" + page
    cid = cid
    quality = 80
    """
    entropy = 'rbMCKn@KuamXWlPMoJGsKcbiJKUfkPF_8dABscJntvqhRSETg'
    appkey, sec = ''.join([chr(ord(i) + 2) for i in entropy[::-1]]).split(':')
    params = 'appkey=%s&cid=%s&otype=json&qn=%s&quality=%s&type=' % (appkey, cid, quality, quality)
    chksum = hashlib.md5(bytes(params + sec, 'utf8')).hexdigest()
    url_api = 'https://interface.bilibili.com/v2/playurl?%s&sign=%s' % (params, chksum)
    # print(url_api)
    headers = {
        'Referer': start_url,  # 注意加上referer
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 '
                      'Safari/537.36 '
    }
    # print(url_api)
    html = requests.get(url_api, headers=headers).json()
    # print(json.dumps(html))
    video_list = []
    for i in html['durl']:
        video_list.append(i['url'])
    # print(video_list)
    return video_list


# 获取文件大小
def getDocSize(path):
    try:
        size = os.path.getsize(path)
#         return formatSizeze(size)
        return size
    except Exception as err:
        return 0


def down_video(start_url, url, part):
    vid_headers = {
        'Origin': 'https://www.bilibili.com',
        'Referer': start_url,
        'Range': 'bytes=%d-' % os.path.getsize(part),
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    # with eventlet.Timeout(150,False):#设置超时时间为10秒
    resp = requests.get(url[0], headers=vid_headers, stream=True)
    content_size = int(resp.headers['content-length'])
    # print(content_size)
    # print(getDocSize(part))
    if getDocSize(part) < content_size:
        with open(part, "wb") as f:
            file_big = round(float(content_size / 1024 / 1024), 4)
            print(f"文件大小：  {file_big}  [MB]")
            for data in tqdm(iterable=resp.iter_content(1024), total=file_big * 1024, unit='KB', desc=part.split('/')[-1]):
                f.write(data)
    else:
        print(f'{part} 文件已经下载完成')
    semlock.release()

def makdir(url):
    if url.isdigit() == True:  # 如果输入的是BV号
        # 获取cid的api, 传入aid即可
        start_url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + url

    else:
        # https://www.bilibili.com/video/BV46958874/?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.16
        start_url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + re.search(r'BV([0-9a-zA-Z]*)', url).group(
            1)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
    html = requests.get(start_url, headers=headers).json()
    data = html['data']
    currentVideoPath = os.path.join(path, data['title'])  # 当前目录作为下载目录
    # 创建文件夹存放下载的视频
    if not os.path.exists(currentVideoPath):
        os.makedirs(currentVideoPath)
    return currentVideoPath


def BV_jiexi(url):
    f_path = makdir(url)
    start_url = 'https://api.bilibili.com/x/player/pagelist?bvid=' + re.search(r'BV([0-9a-zA-Z]*)', url).group(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    data = requests.get(start_url, headers=headers).json()['data']
    shuju = []
    for i in data:
        canshu = {}
        canshu['cid'] = i['cid']
        canshu['page'] = i['page']
        canshu['part'] = f_path+'/'+i['part'] + '.mp4'
        canshu['duration'] = i['duration']
        canshu['start_url'] = start_url
        print(f"正在请求:  {i['part'] + '.mp4'}")
        canshu['url'] = get_play_list(start_url, str(i['cid']),)
        shuju.append(canshu)
    return shuju
    # # currentVideoPath = os.path.join(sys.path[0], 'bilibili_video')  # 当前目录作为下载目录
    # if sys.platform.startswith('win'):
    #     os.startfile(path)

def main():
    threadpool =[]
    # for canshu in BV_jiexi('BV1CK411A7DY'):
    # 少量的 （2p） https://www.bilibili.com/video/BV1T64y1F728
    for canshu in BV_jiexi(input("输入要下载的视频链接或者BV号:  ")):
        semlock.acquire()
        # down_video(canshu['start_url'],canshu['url'], canshu['part'])
        t1 = threading.Thread(target=down_video, args=(canshu['start_url'],canshu['url'], canshu['part']))
        threadpool.append(t1)
        t1.start()


if __name__ == '__main__':
    main()
