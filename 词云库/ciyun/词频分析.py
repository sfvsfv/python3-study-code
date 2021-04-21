# 主要功能自定义设置
Analysis_text = '分析文档.txt'        # 分析文档
userdict = '用户词典.txt'             # 用户词典
StopWords = '停用词库.txt'            # 停用词库
number = 50                       # 统计个数
Output = '词频.txt'                   # 输出文件
background = '词频背景.jpg'           # 词频背景

# 导入扩展库
import re                           # 正则表达式库
# import jieba                        # 结巴分词
import jieba.posseg                 # 词性获取
import collections                  # 词频统计库
import numpy                        # numpy数据处理库
from PIL import Image               # 图像处理库
import wordcloud                    # 词云展示库
import matplotlib.pyplot as plt     # 图像展示库（这里以plt代表库的全称）

# 读取文件
fn = open(Analysis_text,'r',encoding = 'UTF-8')  # 打开文件
string_data = fn.read()                          # 读出整个文件
fn.close()                                       # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式（空格等）
string_data = re.sub(pattern, '', string_data)     # 将符合模式的字符去除

# 动态调整词典
jieba.suggest_freq('川川', True)     #True表示该词不能被分割，False表示该词能被分割

# 添加用户词典
jieba.load_userdict(userdict)

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all=False, HMM=True)    # 精确模式分词+HMM
object_list = []

# 去除停用词（去掉一些意义不大的词，如标点符号、嗯、啊等）
with open(StopWords, 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
for word in seg_list_exact:         # 循环读出每个分词
    if word not in stopwords:       # 如果不在去除词库中
        object_list.append(word)    # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list)       # 对分词做词频统计
word_counts_top = word_counts.most_common(number)    # 获取前number个最高频的词

# 英文词性转中文词性字典：简洁版
En2Cn = {
    'a'    : '形容词',
    'ad'   : '形容词',
    'ag'   : '形容词',
    'al'   : '形容词',
    'an'   : '形容词',
    'b'    : '区别词',
    'bl'   : '区别词',
    'c'    : '连词',
    'cc'   : '连词',
    'd'    : '副词',
    'e'    : '叹词',
    'eng'  : '英文',
    'f'    : '方位词',
    'g'    : '语素',
    'h'    : '前缀',
    'i'    : '成语',
    'j'    : '简称略语',
    'k'    : '后缀',
    'l'    : '习用语',
    'm'    : '数词',
    'mq'   : '数量词',
    'n'    : '名词',
    'ng'   : '名词',
    'nl'   : '名词',
    'nr'   : '名词',
    'nr1'  : '名词',
    'nr2'  : '名词',
    'nrf'  : '名词',
    'nrfg' : '名词',
    'nrj'  : '名词',
    'ns'   : '名词',
    'nsf'  : '名词',
    'nt'   : '名词',
    'nz'   : '名词',
    'o'    : '拟声词',
    'p'    : '介词',
    'pba'  : '介词',
    'pbei' : '介词',
    'q'    : '量词',
    'qt'   : '量词',
    'qv'   : '量词',
    'r'    : '代词',
    'rg'   : '代词',
    'rr'   : '代词',
    'rz'   : '代词',
    'rzs'  : '代词',
    'rzt'  : '代词',
    'rzv'  : '代词',
    'ry'   : '代词',
    'rys'  : '代词',
    'ryt'  : '代词',
    'ryv'  : '代词',
    's'    : '处所词',
    't'    : '时间词',
    'tg'   : '时间词',
    'u'    : '助词',
    'ude1' : '助词',
    'ude2' : '助词',
    'ude3' : '助词',
    'udeng': '助词',
    'udh'  : '助词',
    'uguo' : '助词',
    'ule'  : '助词',
    'ulian': '助词',
    'uls'  : '助词',
    'usuo' : '助词',
    'uyy'  : '助词',
    'uzhe' : '助词',
    'uzhi' : '助词',
    'v'    : '动词',
    'vd'   : '动词',
    'vf'   : '动词',
    'vg'   : '动词',
    'vi'   : '动词',
    'vl'   : '动词',
    'vn'   : '动词',
    'vshi' : '动词',
    'vx'   : '动词',
    'vyou' : '动词',
    'w'    : '标点符号',
    'wb'   : '标点符号',
    'wd'   : '标点符号',
    'wf'   : '标点符号',
    'wj'   : '标点符号',
    'wh'   : '标点符号',
    'wkz'  : '标点符号',
    'wky'  : '标点符号',
    'wm'   : '标点符号',
    'wn'   : '标点符号',
    'wp'   : '标点符号',
    'ws'   : '标点符号',
    'wt'   : '标点符号',
    'ww'   : '标点符号',
    'wyz'  : '标点符号',
    'wyy'  : '标点符号',
    'x'    : '字符串',
    'xu'   : '字符串',
    'xx'   : '字符串',
    'y'    : '语气词',
    'z'    : '状态词',
    'un'   : '未知词',
}

# 输出至工作台，并导出“词频.txt”文件
print ('\n词语\t词频\t词性')
print ('——————————')
fileOut = open(Output,'w',encoding='UTF-8')     # 创建文本文件；若已存在，则进行覆盖
fileOut.write('词语\t词频\t词性\n')
fileOut.write('——————————\n')
count = 0
for TopWord,Frequency in word_counts_top:                       # 获取词语和词频
    for POS in jieba.posseg.cut(TopWord):                       # 获取词性
        if count == number:
            break
        print(TopWord + '\t',str(Frequency) + '\t',list(En2Cn.values())[list(En2Cn.keys()).index(POS.flag)])                    # 逐行输出数据
        fileOut.write(TopWord + '\t' + str(Frequency) + '\t' + list(En2Cn.values())[list(En2Cn.keys()).index(POS.flag)] + '\n') # 逐行写入str格式数据
        count += 1
fileOut.close()                                                 # 关闭文件


print ('\n开始制作词云……')                    # 提示当前状态
mask = numpy.array(Image.open(background))      # 定义词频背景
wc = wordcloud.WordCloud(
    font_path = r'E:\word  字体库\simfang.ttf', # 设置字体（这里选择“仿宋”）
    background_color='white',                   # 背景颜色
    mask = mask,                                # 文字颜色+形状（有mask参数再设定宽高是无效的）
    max_words = number,                         # 显示词数
    max_font_size = 150                         # 最大字号
)

wc.generate_from_frequencies(word_counts)                                        # 从字典生成词云
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))                       # 将词云颜色设置为背景图方案
plt.figure('词云')                                                               # 弹框名称与大小
plt.subplots_adjust(top=0.99,bottom=0.01,right=0.99,left=0.01,hspace=0,wspace=0) # 调整边距
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')                       # 处理词云
plt.axis('off')                                                                  # 关闭坐标轴
print ('制作完成！')                                                             # 提示当前状态
print ('\n作者：丨川川丨')
print ('日期：2020.11.29')
plt.show()

# 避免程序运行完成后直接退出
input()
