#登录引导界面
txt =\
'''
1. 添加学生信息
2. 删除学生信息
3. 查询学生信息
4. 退出系统
'''

#检测路径下是否存在通讯录文件，如果没有则建立文件
import os.path
is_exist = os.path.isfile('addressbook.txt')

    #添加联系人
def add():
    print('添加学生信息')   #引导添加
    print('姓名: ', end = '')
    Name = input()      #输入名字
    print('性别: ', end = '')
    Sex = input()       #输入性别
    print('学号: ', end = '')
    studentNumber = input()    #输入学号
    #将通讯录追加到文件末端
    Contacts_file = open('addressbook.txt','a')
    Contacts_file.write(Name+'\t\t\t'+Sex+'\t\t\t'+studentNumber+'\n')     #在文件中以名字，性别，学号格式排列，最后一个学号就直接换行准备下一个
    Contacts_file.close()   #文件写好后就关闭
    print("添加信息成功，已经保存在文档，请前去查看"+'\n')

#删除通讯录中的信息
def delete():
    print('请输入你要删除的学生名字: ', end = '')
    name = input()  #输入需要删除的学生名字
    Contacts_file = open('addressbook.txt', 'r')   #打开文档
    Contacts_list = []
    #将通讯录缓存到列表内，遇到需要删除的通讯录条目则跳过
    for line in Contacts_file.readlines():
        if line.find(name) != -1:
            continue
        Contacts_list.append(line)
    #将通讯录清空，将缓存在列表中的通讯录信息加载进文件内
    Contacts_file = open('addressbook.txt', 'w')
    for i in range(0, len(Contacts_list)):
        Contacts_file.write(Contacts_list[i])
    Contacts_file.close()
    print("该学生信息已经删除，具体可以对照文档查看"+'\n')

#搜索通讯录
def search():
    print('请输入你要查询的人的名字: ',end = '')
    Search_name = input()
    Contacts_file = open('addressbook.txt','r')    #打开通讯录文档
    for line in Contacts_file.readlines():
        String = line
        find = String.find(Search_name)
        if find !=-1 :
            print("此人信息为：")
            print("姓名:"+'\t\t'+'性别:'+'\t\t'+'学号:')
            print(line)
            break
    #若搜索不到，返回Not Found!
    if find == -1:
        print('此人信息不存在')
    Contacts_file.close()

class InputError(Exception):
    '''当输出有误时，抛出此异常'''
    #自定义异常类型的初始化
    def __init__(self, value):
        self.value = value
    # 返回异常类对象的说明信息
    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))


#主函数
def main():
    while True:  # 如果为真
        # try:

        print("欢迎光临学生管理系统，请选择功能对应的数字执行操作:")  # 引导选择
        print(txt)  # 打印引导界面
        choice = int(input())  # 输入序号选择

        try:
            if type(choice) != int:
                raise main()
        except Exception as e:
            print("输入数字类型错误,请重新输入功能对应的数字")
        # 输入错误序号则重启程序，异常处理
        if choice not in [1, 2, 3, 4]:  # 不在这4个序号里
            print('错误选择')  # 打印错误选择
            main()  # 重新开始
            break
        # 输入正确序号执行相应程序
        elif choice == 1:  # 选择序号为1
            add()  # 添加联系人函数启动
        elif choice == 2:  # 选择序号为2
            delete()  # 删除联系人函数启动
        elif choice == 3:  # 选择序号为3
            search()  # 查询联系人函数启动
        elif choice == 4:  # 如果选择序号为5
            break  # 结束执行


if __name__ == '__main__':
    main()