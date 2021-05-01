import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_iris, make_moons, make_circles, make_blobs
from sklearn.metrics import silhouette_score, homogeneity_completeness_v_measure
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

moons = make_moons(500, noise=0.05, random_state=0) #生成两个交织的半圆环（moons）
circles = make_circles(500, noise=0.05, factor=0.5, random_state=1)#生成一个大圆环套小圆环
blobs = make_blobs(500, centers=2, cluster_std = 0.1, center_box = (-1,1), random_state=8)#生成两团点
synthetic_data = {"moons" : moons, "circles" : circles, "blobs" : blobs}


plt.figure(figsize = (18,5))  #创建画板
i = 0
for name, (X, y) in synthetic_data.items():
    plt.subplot(131 + i)  #控制图像位置
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=ListedColormap(['#FF0000', '#0000FF']))  #绘图并控制颜色
    plt.title(name)
    i += 1

plt.savefig("聚类.png",bbox="tight") #保存图片