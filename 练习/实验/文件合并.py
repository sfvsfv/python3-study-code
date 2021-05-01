'''
有两个磁盘文件A.txt和B.txt，各存放一行字符，要求把这两个文件中的信息合并（按字母顺序排列），并输出到一个新文件C中。
'''

fp1, fp2 = open('A.txt', 'r'), open('B.txt', 'r')
fp1_str, fp2_str = fp1.read(), fp2.read()
fp1.close()
fp2.close()

fp = open('t.txt', 'w')
fp_str = list(fp1_str + fp2_str)
fp_str.sort()
fp_str = ''.join(fp_str)
fp.write(fp_str)
fp.close()
