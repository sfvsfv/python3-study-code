import pandas as pd
from snownlp import SnowNLP
import matplotlib.pylab as plt

plt.rcParams['font.sans-serif']=['SimHei']#设置中文显示
plt.rcParams['axes.unicode_minus'] =False

df = pd.read_csv("houlang_comment.csv",encoding='utf-8')


def snownlp_c(element):
    
    try:
        sn=SnowNLP(element)
        return round(sn.sentiments,1)-0.5
    except:
        pass

df['snownlp']=df['评论'].transform(snownlp_c)   #不需要时注释掉,以免浪费性能

# print(df.info())

# snownlp指数与数量

q1 = df.groupby(by='snownlp')['评论'].count().reset_index()
plt.figure()
plt.plot(q1['snownlp'],q1['评论'])
plt.xlabel('snownlp')
plt.ylabel('quantity')
plt.title('snownlp指数与数量')
plt.show()


# snownlp指数与性别

q2 = df.groupby(by='性别')['snownlp'].mean().reset_index()
plt.figure()
plt.bar(q2['性别'],q2['snownlp'])
plt.xlabel('性别')
plt.ylabel('snownlp')
plt.title('snownlp指数与性别')
plt.show()


# 性别分布情况

a=df.groupby(by='性别')['评论'].count().reset_index()
plt.pie(a['评论'],labels=a['性别'],
        labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
        startangle = 90,pctdistance = 0.6)
plt.title('性别分布')
plt.show()







