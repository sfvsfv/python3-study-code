#首先列出我的核心思路：

# 1.图像由“核心变量”完全控制，图像变化的本质是 变量的改变
#
# 2，自上而下式的思考，图像变化的问题将一步步转为 一系列具体的变量修改
#
# 3，“核心变量”在思考过程中并非不可变更，为了写函数方便，可以适当让步

import pygame,random  #导入py游戏模块和随机模块

#核心变量的声明
background = [[0 for i in range(10)]for j in range(21)] #控制界面大小的
active = []

def new_draw():  #这个函数用来画屏幕的
    screen.fill(white)#填充屏幕为白色
    for i in range(1, 21):#i是x轴，宽度为20
        for j in range(10):#j是y周，宽度为10
            bolck = background[i][j]   #方块在这个背景范围内
            if bolck:  #如果是方块
                #pygame.draw.rect该函数是在给定区域绘制矩形,给砖块绘制为蓝色，内部参数是坐标的转换
                pygame.draw.rect(screen, blue, (j * 25 + 1, 500 - i * 25 + 1, 23, 23))

    for i, j in active:
        pygame.draw.rect(screen, blue, (j * 25+1, 500 - i * 25 + 1, 23, 23))

    pygame.display.update()     #执行这个函数来让我们绘制的东西显示在屏幕上
def move_LR(n):  #左右移动
    """n=-1代表向左，n=1代表向右"""
    x, y = centre       #centre是列表
    y += n  #竖直方向要增加（在下落的意思）
    for i, j in active:
        i += x  #“绝对坐标”变更为“中心坐标+相对坐标”
        j += y  #“绝对坐标”变更为“中心坐标+相对坐标”
        if j < 0 or j > 9 or background[i][j]:#如果在坐标范围内或者背景范围内就停止
            break
    else:
        centre.clear()  #否则就清空
        centre.extend([x, y])#clear+extend修改centra，这样就不用将centra传入传出


#定义旋转函数，这部分代码跟上一部分的move_LR函数一样的，所以就不用重复讲解了
def rotate():
    x, y = centre
    l = [(-j, i) for i, j in active]
    for i, j in l:
        i += x
        j += y
        if j < 0 or j > 9 or background[i][j]:
            break
    else:
        active.clear()
        active.extend(l)    ##避免将centra传入传出

#定义方块向下落函数，总体讲解如下：
# 1，检查是否落到底部，是：继续，否：跳出
#
# 2，active的信息转到background，
#
# 3，检查background是否有“行”被填满 是：继续，否：跳至5
#
# 4，清掉满行，补上空行，计分
#
# 5，生成新的active，检查其位置是否被占（被占<=>方块被堆至顶部<=>game over）
def move_down():
    x, y = centre
    x -= 1
    for i, j in active:
        i += x
        j += y
        if background[i][j]:
            break
    else:
        centre.clear()
        centre.extend([x, y])#避免将centra传入传出
        return
    # 如果新位置未被占用 通过return结束


    # 如果新位置被占用则继续向下执行
    x, y = centre
    for i, j in active:
        background[x + i][y + j] = 1

    l = []
    for i in range(1, 20):
        if 0 not in background[i]:
            l.append(i)

    # l装 行号，鉴于删去后，部分索引变化，对其降序排列，倒着删除
    l.sort(reverse=True)#按照降序排序

    for i in l:
        background.pop(i)
        background.append([0 for j in range(10)])
        # 随删随补

    score[0] += len(l)
    pygame.display.set_caption("分数：%d" % (score[0]))#设置标题为分数

    active.clear()#再次清空
    active.extend(list(random.choice(all_block)))#随机选择其中一种方块
    # all_block保存7种形状的信息，手打出来的
    centre.clear()
    centre.extend([20, 4])

    x, y = centre
    for i, j in active:
        i += x
        j += y
        if background[i][j]:
            break
    else:
        return
    alive.append(1)

#组装因为核心变量发生变化,new_draw重写  ，大部分还是跟上面部分的draw差不多，但是核心变量变化，所以必须重写
def new_draw():
    screen.fill(white)#屏幕白色

    for i in range(1, 21):
        for j in range(10):
            bolck = background[i][j]
            if bolck:
                pygame.draw.rect(screen, blue, (j * 25 + 1, 500 - i * 25 + 1, 23, 23))

    x, y = centre #x,y的列表
    for i, j in active:
        i += x
        j += y
        pygame.draw.rect(screen, blue, (j * 25 + 1, 500 - i * 25 + 1, 23, 23))

    pygame.display.update()#绘出来到屏幕
#核心变量定义  可以理解为就是所有的方块
all_block = (((0, 0), (0, -1), (0, 1), (0, 2)),
             ((0, 0), (0, 1), (-1, 0), (-1, 1)),
             ((0, 0), (0, -1), (-1, 0), (-1, 1)),
             ((0, 0), (0, 1), (-1, -1), (-1, 0)),
             ((0, 0), (0, 1), (1, 0), (0, -1)),
             ((0, 0), (1, 0), (-1, 0), (1, -1)),
             ((0, 0), (1, 0), (-1, 0), (1, 1)))
background = [[0 for i in range(10)] for j in range(24)] #生成方块的时的中心为[20,4]可能会有方块伸展到 21 层,然后引发越界错误，所以将上限设为24
background[0] = [1 for i in range(10)]
active = list(random.choice(all_block))     #随机选择其中一个砖块
centre = [20, 4]
score = [0]
for i in range(1, 20):
        if 0 not in background[i]:
            l.append(i)
pygame.init()
screen = pygame.display.set_mode((250, 500))
pygame.display.set_caption("俄罗斯方块")
fclock = pygame.time.Clock()    #创建时钟对象 (可以控制游戏循环频率)

black = 0, 0, 0#这是黑色的RGB配色
white = 255, 255, 255   #   白色的RGB为255.255.255
blue = 0, 0, 255#这是蓝色的RGB

times = 0#初始化次数为0
alive = []#定义空列表
press = False#开始的时候没有按，所以开始为false
while True:   #游戏循环 -> 意味着游戏的正式开始！
    for event in pygame.event.get():   #监听用户事件
        if event.type == pygame.QUIT:   # 判断用户是否点击了关闭按钮
            sys.exit()      #按了就结束游戏
        elif event.type == pygame.KEYDOWN:  #如果是键盘被按下
            if event.key == pygame.K_LEFT:  #按下向左键
                move_LR(-1)#就向左移动一格
            elif event.key == pygame.K_RIGHT:   # 按下向右键盘
                move_LR(1)      #就向右移动一个格
            elif event.key == pygame.K_UP:      #按向上键
                rotate()#那就旋转
            elif event.key == pygame.K_DOWN:    #按向下键
                press = True    #press就变为True,，可以连续向下移动
        elif event.type == pygame.KEYUP:    #按住向上键
            if event.key == pygame.K_DOWN:  #如果按向下键盘
                press = False#就不会再连续下降，press变为false
    if press:   #如果一直按住向下
        times += 10#次数就加10

    if times >= 50:#次数大于50
        move_down()#向下移动
        times = 0#次数归0
    else:#否则次数智能加1
        times += 1

    if alive:
        pygame.display.set_caption("over分数：%d" % (score[0]))#显示所得分数
        time.sleep(3)  #休息3秒
        break#停止
    new_draw()#再重新开始
    fclock.tick(100)#每秒描绘100次
