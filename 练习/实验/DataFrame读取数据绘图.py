'''
利用DataFrame读取score.xlsx文件中的数据，并用matplotlib在坐标系中绘制平均分和直方图，
要求横坐标为人名，纵坐标为所有科目成绩的平均分。最后将结果写入result.xlsx中。(成绩不存在的以0分处理)
'''

import pandas as pd
import matplotlib as plt
#将excel文件读到内存中，形成dataframe,并命名为people
people=pd.read_excel(r'D:\code\python\shiyan\score.xlsx')

#显示前五行(默认)
# print (people.head(10))

df = pd.DataFrame(people)
c=df.mean(axis = 1, skipna = True)
print(c)

#定义ID为索引
# people=people.set_index('name')
#生成output.xlsx文件
# people.to_excel('D:\code\python\shiyan\output.xlsx')





