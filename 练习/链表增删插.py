class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p


class LinkList(object):
    #定义头结点
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print('链表为空！')
            return

        elif key <0  or key > self.getlength():
            print('键入值错误！')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():
            print('链表为空！')
            return

        elif key <0  or key > self.getlength():
            print('键入值错误！')
            return

        else:
            self.delete(key)
            return self.insert(key)

    #初始化链表
    def initlist(self,data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    #获取链表长度
    def getlength(self):

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    #判断链表是否为空
    def is_empty(self):

        if self.getlength() ==0:
            return True
        else:
            return False


    def clear(self):

        self.head = 0

    #单链表添加操作，在尾部添加结点
    def append(self,item):
        #q为待添加的结点
        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q

    #获取结点数据域的值
    def getitem(self,index):

        if self.is_empty():
            print('链表为空！')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:
            print('对象不存在！')

    #链表数据插入操作
    def insert(self,index,item):

        if self.is_empty() or index<0 or index >self.getlength():
            print('链表为空！')
            return

        if index ==0:
            q = Node(item,self.head)
            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p

    #链表数据删除操作
    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            print('链表为空！')
            return

        if index ==0:
            q = Node(item,self.head)
            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next


    def index(self,value):
        if self.is_empty():
            print('链表为空！')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


link = LinkList()
link.initlist([1,2,3,4,5])
print(link.getitem(4))
link.append(6)
print(link.getitem(5))

link.insert(4,40)
print(link.getitem(3))
print(link.getitem(4))
print(link.getitem(5))

link.delete(5)
print(link.getitem(5))

link.index(5)