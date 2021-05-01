import jieba
import collections
import re
import wordcloud
import numpy
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f():
    background = '词频背景.jpg'
    # 数据
    with open('zichan.txt',encoding='utf-8') as f:
        data = f.read()

    # 文本预处理  去除一些无用的字符   只提取出中文出来
    new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
    new_data = " ".join(new_data)

    # 文本分词
    seg_list_exact = jieba.cut(new_data, cut_all=True)

    result_list = []
    with open('stop_words.txt', encoding='utf-8') as f:
        con = f.readlines()
        stop_words = set()
        for i in con:
            i = i.replace("\n", "")   # 去掉读取每一行数据的\n
            stop_words.add(i)

    for word in seg_list_exact:
        # 设置停用词并去除单个词
        if word not in stop_words and len(word) > 1:
            result_list.append(word)
    print(result_list)

    # 筛选后统计
    word_counts = collections.Counter(result_list)
    # 获取前100最高频的词
    word_counts_top100 = word_counts.most_common(100)
    print(word_counts_top100)

    mask = numpy.array(Image.open(background))
    # 绘制词云
    wc = wordcloud.WordCloud(
        background_color='white',  # 设置背景颜色  默认是black
        width=900, height=600,
        max_words=100,            # 词云显示的最大词语数量
        mask=mask,          #词云形状
        font_path='simhei.ttf',   # 设置字体  显示中文
        max_font_size=99,         # 设置字体最大值
        min_font_size=16,         # 设置子图最小值
        random_state=50           # 设置随机生成状态，即多少种配色方案
    ).generate_from_frequencies(word_counts)
    wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
    # 显示生成的词云图片
    plt.imshow(wc, interpolation='bilinear')
    # 显示设置词云图中无坐标轴
    plt.axis('off')
    plt.show()


def f1():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来显示中文，不然会乱码
    plt.rcParams['axes.unicode_minus'] = False      #字符显示
    plt.rcParams['lines.linewidth'] =4  #线条宽度为4
    #读取数据转换为数组，文件必须用gbk方式打开
    data = pd.read_csv("gong.csv",encoding='gbk')
    data = np.array(data)
    print(data)  #打印看下文件的内容
    # data是一个多维数组，所以可以用data[:,1]这种分片操作取某一列的值
    plt.pie(data[:, 1], labels=data[:, 0], autopct="%.1f")
    plt.title('不同项目的账面价值')  #标题
    plt.show()  #显示
# def f4():
    plt.plot(data[:, 0], data[:, 1])
    plt.xlabel("项目")  #以评估价值画折线图
    plt.ylabel("账面价值")
    plt.show()

f()
f1()
