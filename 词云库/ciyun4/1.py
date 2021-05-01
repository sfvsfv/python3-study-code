# import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import wordcloud
import jieba
import csv

def func1():
	file = open('caiwu.txt',encoding="utf-8")
	result = file.read()
	file.close()
	return result

def func2():
	file = open('财务报表.csv',encoding="gbk")
	reader = csv.reader(file)
	c = []
	v = []

	for row in reader:
		c.append(row[1])
		v.append(row[2])
	file.close()
	return c, v

def func3(words):
	wordList = jieba.lcut(words)
	invalid = ['的','和','有','之','在','于','中','下','是','了',\
		'用','与','及','等','到','它','其','J','A','F','L','H','R']
	mk = np.array(Image.open("词频背景.jpg"))
	c = wordcloud.WordCloud(scale=4,stopwords=invalid,mask=mk,\
		font_path="msyh.ttf")
	c.generate(" ".join(wordList))
	c.to_file('./词云.jpg')

def func4(c, v):
	plt.rcParams['font.family']=['KaiTi']
	params = {
    'figure.figsize': '8, 4'
	}
	plt.rcParams.update(params)
	width = 0.3
	num1 = [float(i) for i in c[1:]]#从第二行到最后一行
	num2 = [float(i) for i in v[1:]]
	x = list(range(len(num1)))
	x = [str(i) for i in x]
	plt.figure(1)
	plt.subplot(1, 2, 1)
	plt.bar(x, num1, width=width, fc='crimson')
	plt.xlabel("2000年开始第n年")
	plt.ylabel(c[0])
	plt.figure(1)
	plt.subplot(1, 2, 2)
	plt.bar(x, num2, width=width, fc='seagreen')
	plt.xlabel("2000年开始第n年")
	plt.ylabel(v[0])
	plt.savefig('./图表.jpg')

def func5(c, v):
	num1 = [float(i) for i in c[1:]]
	num2 = [float(i) for i in v[1:]]
	return np.mean(num1), np.mean(num2)

def func6(c, v):
	num1 = [float(i) for i in c[1:]]
	num2 = [float(i) for i in v[1:]]
	return np.var(num1), np.var(num2)

words = func1()
c, v = func2()
func3(words)
func4(c, v)



