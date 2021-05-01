import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import wordcloud
import jieba
import csv

def w1():
	file = open('秋季赛赛程介绍.txt',encoding="gbk")
	result = file.read()
	file.close()
	return result

def w2():
	file = open('秋季赛常规赛.csv',encoding="gbk")
	reader = csv.reader(file)
	c = []
	v = []

	for row in reader:
		c.append(row[1])
		v.append(row[2])
	file.close()
	return c, v

def w3(danci):
	wordList = jieba.lcut(danci)
	invalid = ['的','和','有','之','在','于','中','下','是','了',\
		'用','与','及','等','到','它','其','J','A','F','L','H','R']
	mk = np.array(Image.open("lu.jpg"))
	c = wordcloud.WordCloud(scale=4,stopwords=invalid,mask=mk,\
		font_path="msyh.ttf")
	c.generate(" ".join(wordList))
	c.to_file('./词云.jpg')

def w4(c, v):
	plt.rcParams['font.family']=['KaiTi']
	params = {
    'figure.figsize': '8, 4'
	}
	plt.rcParams.update(params)
	width = 0.3
	num1 = [float(i) for i in c[1:]]
	num2 = [float(i) for i in v[1:]]
	x = list(range(len(num1)))
	x = [str(i) for i in x]
	plt.figure(1)
	plt.subplot(1, 2, 1)
	plt.bar(x, num1, width=width, fc='crimson')
	plt.xlabel("组别")
	plt.ylabel(c[0])
	plt.figure(1)
	plt.subplot(1, 2, 2)
	plt.bar(x, num2, width=width, fc='seagreen')
	plt.xlabel("组别")
	plt.ylabel(v[0])
	plt.savefig('./图表.jpg')

def w5(c, v):
	num1 = [float(i) for i in c[1:]]
	num2 = [float(i) for i in v[1:]]
	return np.min(num1,axis=0), np.max(num2,axis=0)

# def w6():
# 	n1=0
# 	n2=0
# 	d=open('秋季赛赛程介绍.txt','r',encoding='gbk')
# 	f=d.read()
# 	c=len(f)
# 	print("文档总字数为：",c)
def w6():
	txt = open("秋季赛赛程介绍.txt", "r", encoding="gbk").read()
	words = jieba.lcut(txt)  # 对文本进行分词处理
	counts = {}  # 构造字典
	for word in words:
		if len(word) == 1:
			continue
		else:
			counts[word] = counts.get(word, 0) + 1
	items = list(counts.items())
	items.sort(key=lambda x: x[1], reverse=True)
	for i in range(50):
		word, count = items[i]
		print("{0:<10}{1:>5}".format(word, count))


danci = w1()
c, v = w2()
w3(danci)
w4(c, v)
max=w5(c,v)
min=w5(c,v)
w6()

print("胜场最多净胜分1",max)
print("胜场最少净胜分2：",min)


