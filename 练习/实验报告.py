#a=[{'职业':'诗人','爱好':'喝酒','姓名':'李白'},{'职业':'工程师','爱好':'读书','姓名':'张明'}]
#for i in a.keys():
 #   print("key:"+i+"value"+a)

#i=9
#while i>=1:
#    j=1
 #   while j<=i:
 #       print('%d*%d=%d '%(j,i,j*i),end='')
  #      j+=1
 #   print()
 #   i-=1


# def angle(a, b, c):
#     if (a<=0 or b<=0 or c<=0):
#         return -1
#     elif((a+b)>c and (a+c)>b and (b+c)>a):
#         return 1
#     else:
#         return 0
# m=input("请输入a,b,c大小",(%a,%b,%c))
# return


#登录引导界面
txt = '''
1. add contacts
2. delete contacts
3. search contacts
4. show all contacts
5. exit the system 
'''

#检测路径下是否存在通讯录文件，如果没有则建立文件
import os.path
is_exist = os.path.isfile('addressbook.txt')
if is_exist == 0:
    new_file = open('Contacts.txt', 'w')
    new_file.close()

#入口程序
def start():
    #设置循环，当用户输入特定选项退出
    while True:
        print("Welcome, select a number:")
        print(txt)
        userchoice = int(input())
        #输入错误序号则重启程序
        if userchoice not in [1,2,3,4,5]:
            print('wrong choice')
            start()
            break
        #输入正确序号执行相应程序
        elif userchoice == 1:
            add_contacts()
        elif userchoice == 2:
            delete_contacts()
        elif userchoice == 3:
            search_contacts()
        elif userchoice == 4:
            show_all_contacts()
        elif userchoice == 5:
            break

#添加联系人
def add_contacts():
    print('Add new contacts')
    print('Name: ', end = '')
    Name = input()
    print('Sex: ', end = '')
    Sex = input()
    print('Relationship(Friend/ Family/ Classmate): ', end = '')
    Relationship = input()
    print('Number: ', end = '')
    Number = input()
    #将通讯录追加到文件末端
    Contacts_file = open('Contacts.txt','a')
    Contacts_file.write(Name+'\t'+Sex+'\t'+Relationship+'\t'+Number+'\n')
    Contacts_file.close()

#删除通讯录中的信息
def delete_contacts():
    print('Enter the name: ', end = '')
    name = input()
    Contacts_file = open('Contacts.txt', 'r')
    Contacts_list = []
    #将通讯录缓存到列表内，遇到需要删除的通讯录条目则跳过
    for line in Contacts_file.readlines():
        if line.find(name) != -1:
            continue
        Contacts_list.append(line)
    #将通讯录清空，将缓存在列表中的通讯录信息加载进文件内
    Contacts_file = open('Contacts.txt', 'w')
    for i in range(0, len(Contacts_list)):
        Contacts_file.write(Contacts_list[i])
    Contacts_file.close()

#搜索通讯录
def search_contacts():
    print('Enter the name: ',end = '')
    Search_name = input()
    Contacts_file = open('addressbook.txt','r',encoding='utf-8')
    for line in Contacts_file.readlines():
        String = line
        find_or_not = String.find(Search_name)
        if find_or_not !=-1 :
            print(line)
            break
    #若搜索不到，返回Not Found!
    if find_or_not == -1:
        print('Not Found!')
    Contacts_file.close()

#显示通讯录所有条目
def show_all_contacts():
    print('Name\tSex\tRelationship\tNumber', end = '\n')
    Contacts_file = open('addressbook.txt','r')
    print(Contacts_file.read())
    Contacts_file.close()

#执行入口程序
start()
