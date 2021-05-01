import pandas as pd

df = pd.read_excel("score.xlsx",index_col='name')
df.head()

# 空值替换
df = df.fillna(0)
df['mean']=  df.mean(axis=1)
df['mean'].plot.bar()
df.to_excel("result.xlsx")
print('处理完成')