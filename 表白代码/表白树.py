import turtle#导入海龟图模块（个人喜欢这么叫）
import random#导入随机模块
def love(x,y):#定义函数画爱心，在(x,y)处画爱心
# turtle模块的的Turtle函数，就是把绘图模块传递给lv，后面写代码就不用一直写turtle.Turtle()，直接用lv代替了。
    lv=turtle.Turtle()
    lv.hideturtle()#隐藏画笔的turtle形状
    lv.up()#拿起笔
    lv.goto(x,y)#把笔定位放到坐标(x,y)处
    def curvemove():#定义个函数，画圆弧
        for i in range(20): #遍历0到19，理解为20次循环
            lv.right(10)#右转移动10度
            lv.forward(2)#向当前画笔方向移动2个像素长度
    lv.color('red','pink')#这个函数是用画笔为红色，粉色两种（红色写字，粉丝填充爱心）
    lv.speed(10)#画笔的速度（范围为1到10）
    lv.pensize(1)#画笔的宽度大小，就是我们理解的笔芯粗细为1
    #开始画爱心
    lv.down()#移动时绘制图形（就是拿着笔移动，移动的时候把东西要画上去）
    lv.begin_fill()#英文很明确，就是开始填充图形
    lv.left(140)#逆时针移动140度
    lv.forward(22)#向前移动22个像素长度
    curvemove()#调用定义的函数
    lv.left(120)#逆时针旋转120度
    curvemove()#再次调用函数
    lv.forward(22)#向前移动22个像素长度
    lv.write("思思",font=("Arial",12,"normal"),align="center")#这我就定义的女朋友的小名，楷体，字体大小12，正常，居中
    lv.left(140)#逆时针旋转140度
    lv.end_fill()#画完，结束填充

def tree(branchLen,t):  #上面我们画了爱心，现在我们要画树，于是定于树这个函数，对应内部为树枝
    if branchLen > 5:#剩余树枝太少要结束递归
        if branchLen<20:#如果树枝剩余长度较短则变绿
            t.color("green")#画笔颜色为绿色
            # 画笔大小随机控制在这两个参数范围内，random.uniform(x, y) 方法将随机生成一个实数，它在 [x,y] 范围内
            t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
            t.down()#画笔移动时绘制图形
            t.forward(branchLen)#画笔向前移动branchlen（树枝长度）个像素长度
            love(t.xcor(),t.ycor())#返回（x,y）现在坐标是多少
            t.up()#拿起笔
            t.backward(branchLen)#画笔后移动branchlen个像素长度
            t.color("brown")#后退时，颜色为棕色
            return #返回结果
        t.pensize(random.uniform((branchLen+5)/4-2,(branchLen+6)/4+5))#跟上面一样，画笔大小控制在一个范围，保证树枝不是一样大的
        t.down()#移动时绘制图形（就是拿着笔移动，移动的时候把东西要画上去）
        t.forward(branchLen)#向前移动branchlen个像素长度
        # 以下递归
        ang=random.uniform(15,45)#递归传递参数到定义的函数里去，这样branchlen就有具体大小了
        t.right(ang)#顺时针偏转ang度，ang大小在15到45范围
        tree(branchLen-random.uniform(12,16),t)#随机决定减小长度
        t.left(2*ang)#逆时针转动2*ang，ang范围为12到16
        tree(branchLen-random.uniform(12,16),t)#随机决定减小长度
        t.right(ang)#顺时针转动ang长度
        t.up()#拿起笔
        t.backward(branchLen)#后退移动branchlen（15）像素长度

myWin = turtle.Screen()#定义一个tuetle屏幕
t = turtle.Turtle()#把绘图模块传给t
t.hideturtle()#把画笔藏起来
t.speed(10)#画笔速递为10
t.left(90)#画笔逆时针转动90度
t.up()#提起笔
t.backward(200)#画笔后退移动200个像素单位
t.down()#移动时绘制图形（就是拿着笔移动，移动的时候把东西要画上去）
t.color("brown")#后退移动时颜色为棕色
t.pensize(32)#后退画笔大小为32
t.forward(60)#再向前移动60
tree(100,t)#传递参数100给branchlen
myWin.exitonclick()#点击结束

