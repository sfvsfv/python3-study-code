import csv
# with open('data.csv','w',encoding='gbk') as f:  #如果是csv一定要用gbk编译方式，utf-8乱码
#     writer=csv.writer(f)#writer方法初始化写入对象
#     writer.writerow(['id','name','age'])#writerow写入每一行数据
#     writer.writerow(['1','川川','20'])
#     writer.writerow(['3','笨笨','21'])
#     writer.writerow(['4','憨憨','21'])

with open('bb.csv','w',encoding='gbk') as f:
    # writer=csv.writer(f,delimiter=' ')#writer方法初始化写入对象
    # writer.writerow(['id','name','age'])#writerow写入每一行数据
    # writer.writerow(['1','川川','20'])
    # writer.writerow(['3','笨笨','21'])
    # writer.writerow(['4','憨憨','21'])

    # writer.writerow(['id','name','age'])
    # writer.writerow([['1','川川','20'],['3','笨笨','21'],['4','憨憨','21']])
    filename=['id','age','interest']
    writer=csv.DictWriter(f,fieldnames=filename)#初始化字典
    writer.writeheader()#写入头信息
    writer.writerow({'id':'1001','age':'15','interest':'play'})
    writer.writerow({'id':'1002','age':'25','interest':'ll'})