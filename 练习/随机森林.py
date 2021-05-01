import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, roc_auc_score, f1_score, log_loss
from sklearn.datasets import load_iris, load_boston, make_moons, make_circles, make_classification
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
pd.set_option('mode.chained_assignment',None)
 #导入需要用的包
boston = load_boston()
boston_X = boston.data
boston_y = boston.target
boston_train_X, boston_test_X, boston_train_y, boston_test_y = train_test_split(boston_X, boston_y, test_size = 0.2, random_state = 123)
#创建模型，得到数据
clf = RandomForestRegressor(random_state = 123)
clf.get_params()
#得到超参数列表和每个超参数的默认值
param_grid = {'n_estimators': [10,20,50], 'max_features': [3,5,7]}
kf = KFold(n_splits=3, shuffle=True, random_state=123)
gs = GridSearchCV(clf, param_grid, 'r2', cv = kf)
gs.fit(boston_train_X, boston_train_y)
cv_results = pd.DataFrame(gs.cv_results_)
cv_results
# 使用3折交叉验证做超参数的网格搜索
gs.best_estimator_
# 得到最优超参数组合的随机森林回归模型。
fig, ax = plt.subplots()#等价于：fig = plt.figure()   ax = fig.add_subplot(1,1,1)
grouped = cv_results.groupby('param_max_features')
for key, group in grouped:
    group.plot(ax=ax, x='param_n_estimators', y='mean_test_score', label=key)
plt.savefig("随机森林.png",box="tight")#保存图片去除空白部分


