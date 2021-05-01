# import csv
# with open('bb.csv','r',encoding='utf-8') as f:
#     r=csv.reader(f)
#     for row in r:
#         print(row)
import pandas as pd
d=pd.read_csv('bb.csv')
print(d)