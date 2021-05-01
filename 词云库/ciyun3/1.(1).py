import csv
import jieba
import wordcloud
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def f1():
    fp=open("词云(1).txt","rt")
    txt=fp.read()
    l=jieba.lcut(txt)
    return l
def f2():
    csvfile=open("食品质量.csv","r",encoding='gbk')
    reader=csv.reader(csvfile)
    list1=[]
    list2=[]
    list3=[]
    for line in reader:
        list1.append(line[0])
        list2.append(line[1])
        list3.append(line[2])
    list1.remove("食品名称(100克)")
    list2.remove("蛋白质含量(克)")
    list3.remove("碳水化合物含量(克)")
    csvfile.close()
    return list1,list2,list3 
def f3(n):
    s=" ".join(n)
    im=Image.open("lu.jpg")
    tux=np.array(im)
    w=wordcloud.WordCloud(background_color="pink", \
                                               font_path="msyh.ttf",mask=tux)
    w.generate(s)
    w.to_file("1.png")
    return
def f4(a,c):
    y1=[]
    for t in c:
        y1.append(int(t))
    plt.rcParams["font.family"]="SimHei"
    plt.subplot(121)
    plt.bar(a,y1,color="pink",width=0.3)
    plt.subplot(122)
    plt.pie(y1,autopct="%0.2f%%")
    plt.show()
def f5():
    n1=0
    n2=0
    d=open('词云(1).txt','r',encoding='gbk')
    f=d.read()
    c=len(f)
    print("文档总字数为：",c)
    for i in f:
        if  '0'<=i<='9':
            n1=n1+1
        else:
            n2=n2+1
    print("数字个数:",n1)
    print("文字个数：",n2)


a=f1()
f3(a)
d,b,c=f2()
f4(d,c)
f5()





















