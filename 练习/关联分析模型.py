import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
# 读取鸢尾花卉数据集。
iris = load_iris()
iris_X = iris.data
iris_y = iris.target

pca = PCA()
pc = pca.fit_transform(iris_X)
#调用主成分分析器的函数fit_transform()做训练和变换，返回主成分
pca.explained_variance_ratio_
#得到每个主成分能解释的总体方差比例。

pca = PCA(2)
pc = pca.fit_transform(iris_X)
pc[:5]

pca.components_

plt.figure(figsize = (8,6))
plt.scatter(pc[:, 0], pc[:, 1], c=iris_y, cmap=ListedColormap(['darkorange', 'c', 'darkblue'])) #绘制点和颜色

plt.savefig("鸢尾.png",bbox_inches="tight")#保存图片，出去空白多余部分
