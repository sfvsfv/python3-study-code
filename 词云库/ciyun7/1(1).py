import jieba
import wordcloud
import numpy as np
from PIL import Image
import matplotlib. pyplot as plt
import pandas as pd

def f1():
    a=open("房地产价格评估.txt","rt")
    b=a.read()
    a.close()
    return b

def f2(b):
    list1=jieba.lcut(b)
    c=" ".join(list1)
    im=Image.open("1.jpg")
    tux=np.array(im)
    w=wordcloud.WordCloud(width=1000,height=1500,background_color="pink",  font_path="msyh.ttf",mask=tux)
    w.generate(c)
    w.to_file("1.png")
b=f1()
f2(b)

def f3():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来显示中文，不然会乱码
    plt.rcParams['lines.linewidth'] =4  #线条宽度为4
    #读取数据转换为数组，文件必须用gbk方式打开
    data = pd.read_csv("房地产评估.csv",encoding='gbk')
    data = np.array(data)#转换为数组
    print(data)  #打印看下文件的内容

    # data是一个多维数组，所以可以用data[:,1]这种分片操作取某一列的值
    plt.pie(data[:, 1], labels=data[:, 0], autopct="%.1f%%")
    plt.title('房地产评估')  #标题
    # plt.show()  #显示
    plt.savefig("图表.png")
f3()



    
