'''
将文件a.txt的字符串前加上序号“1：”、“2：”、…。
'''

f1=open('a (3).txt')

b=f1.readlines()
for i in range(0,len(b)):
     b[i]=str(i+1)+': '+b[i]

f1.close()
f2=open('a2.txt','w')
f2.writelines(b)
f2.close()