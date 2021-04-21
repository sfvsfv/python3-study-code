from collections import defaultdict
import importlib
import sys
importlib.reload(sys)
import warnings
warnings.filterwarnings("ignore")

class LBTrie:
    def __init__(self): #初始化
        self.trie = {}  #树为空列表
        self.size = 0   #大小开始为0
    #添加单词
    def add(self, word):
        p = self.trie   #空列表传给p
        dicnum = 0      #开始单词为0

        word = word.strip() #返回移除字符串头尾指定的字符生成的新字符串给word
        for c in word:  #对于在word里面的单词
            if not c in p:      #如果c在p中为假，以实就是c不在p中
                p[c] = {}       #列表p里面的c为空值（就是不在的意思）
            dicnum+=1   #单词数量就加一
            p = p[c]    #就把c放到p里面


        if word != '':
            #在单词末尾处添加键值''作为标记，即只要某个字符的字典中含有''键即为单词结尾
            p[''] = ''
        if dicnum == len(word):     #如果数量等于word的长度
            return True #返回真值
    #查询单词
    def search(self, word):
        p = self.trie
        word = word.lstrip()    #截掉字符串左边的空格或指定字符
        for c in word:
            if not c in p:
                return False
            p = p[c]
        #判断单词结束标记''
        if '' in p: #如果空格在p里面
            return True #返回真值
        return False
    def cipin(self):
        total = 0
        with open('冰与火之歌.txt') as f:
            b=input("请输入你要统计哪个单词的词频：")
            for line in f:
                finded = line.find(b)        #查询line里面的b
                if finded != -1 and finded != 0:
                    total += 1
        print("词频为：", total)
    #打印Trie树的接口
    def output(self):       #定义输出口函数
        self.__print_item(self.trie)    #定义这个接口
        return  self.__print_item(self.trie)    #返回列表

    #实现Trie树打印的私有递归函数，indent控制缩进
    def __print_item(self, p, indent=0):
        if p:
            ind = '' + '\t' * indent    #缩进长度等于空格加in*\t
            for key in p.keys():    #对于在字典的键
                label = "'%s' : " % key #把键传给label
                print(ind + label + '{'  )  #打印
                self.__print_item(p[key], indent+1)#调用上面的接口返回值

            print (ind + ' '*len(label) + '}'   )   #打印出来

def codeutil(strs):
         return strs.encode(encoding='utf-8',errors='strict')

if __name__ == '__main__':      #主函数调用
    trie_obj = LBTrie()
    c=trie_obj.cipin()
    #添加单词
    corpus = open('冰与火之歌.txt','r')#文本内容
    # tree = open('a.txt','w+')#追加内容
    countdic = defaultdict(int)
    for record in corpus.readlines():
        recordlist = record.split(' ')
        for word in recordlist:
            check = trie_obj.add(codeutil(word))
            if check:
                countdic[word] += 1
    resortedcountdic = sorted(countdic.items(), key=lambda item: item[1], reverse=True)
    a=input("请输入你要查询的哪个单词是否存在：")
    if trie_obj.search(codeutil(a)):  # 在这输入你想要查询的单词会显示是否存在
        print('该单词存在')
    else:
        print('该单词不存在')
