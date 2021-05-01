# sys是python的标准库
# 提供了python运行时环境变量的操控
# sys.exit()用于结束游戏退出
import sys
import pygame
import random

# 游戏的高宽
WIDTH, HEIGHT = 640, 360
# WIDTH, HEIGHT = 1280, 720
# 把颜色值(230, 230, 230)赋值给 bg_color 变量
# 三个整数依次是三原色中红色、绿色和蓝色的浓度值。浓度值是一个整数，最大为255，最小为0。
bg_color = (255, 255, 255)
button_text_list = ['川川比易烊千玺帅亿点', '川川脾气好', '川川会洗衣服还会做饭', '川川体贴','川川很温柔']


# 点击喜欢按钮后显示的页面
def show_like_interface(text, screen, color=(255, 0, 0)):
    screen.fill(bg_color)
    font = pygame.font.Font('./font/simkai.ttf', WIDTH // (len(text)))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH / 2, HEIGHT / 2)
    screen.blit(textRender, textRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# 按钮
def button(text, x, y, w, h, color, screen):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.Font('./font/simkai.ttf', 20)
    textRender = font.render(text, True, (0, 0, 0))
    textRect = textRender.get_rect()
    textRect.center = ((x + w / 2), (y + h / 2))
    screen.blit(textRender, textRect)


# 标题
def title(text, screen, scale, color=(0, 0, 0)):
    # pygame.font.Font("字体","字号"，*)
    font = pygame.font.Font('./font/simkai.ttf', WIDTH // (len(text) * 2))
    # 使用已有的文本创建一个位图image，返回值为一个image;对于位图可用get_height(),get_width()的方法获得高与宽；True表示是否抗锯齿，第三个为字体颜色，还可以有第四个为背景色，没有时就为默认的透明；
    textRender = font.render(text, True, color)
    # Rect对象有一些重要的属性，如：top，botton，letf、right表示上下左右
    # width，height表示宽高   我有这些值之后，对于我们编写程序十分方便
    textRect = textRender.get_rect()
    # 中央x坐标整数值 顶部y坐标的整数值
    textRect.midtop = (WIDTH / scale[0], HEIGHT / scale[1])
    # 将位图绘制到屏幕上，screen为建立的主屏；
    screen.blit(textRender, textRect)

    # 生成随机的位置坐标


def get_random_pos():
    x, y = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
    return x, y


def main():
    text = "不行"
    # 在我们要动手用它完成我们的想法之前，电脑这个强迫症需要我们检查一遍，这个工具包是否完整，能否正常给我们提供帮助。而这个检查的动作， pygame.init()   检查，电脑上一些需要的硬件调用接口、基础功能是否有问题。如果有，他会在程序运行之前就反馈给你，方便你进行排查和规避。

    # 对pygame内部各种功能进行初始化创建及变量设置，比如pygmae里面的窗体，键盘的使用的事件队列，等等都需要我们pygame.init()初始化
    pygame.init()
    # 调用 display 模块的 set_mode 函数，作用是初始化屏幕对象（也即窗口对象）。此处传入一个参数，即(640, 360)元组，这使得窗口的分辨率是640*360
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # 窗口标题
    pygame.display.set_caption("川川的表白")
    # 不喜欢按钮的初始位置和大小
    unlike_pos_x = 330
    unlike_pos_y = 250
    unlike_pos_width = 100
    unlike_pos_height = 50

    # 喜欢按钮的初始位置和大小
    like_pos_x = 180
    like_pos_y = 250
    like_pos_width = 100
    like_pos_height = 50
    # 标识位，作为小姐姐之后点击了同意后退出的标准
    running = True
    # 按钮颜色
    like_color = (216, 191, 216)
    while running:

        # 填充屏幕背景色
        # 显示窗口背景填充bg_color眼神
        screen.fill(bg_color)
        # 加载图片,从文件加载新图片
        img = pygame.image.load("./img/3.jpg")
        # Surface对象与图像时一一对应关系
        # 简单理解在pygame里导入的任何图片都是Surface对象
        # pygame使用内部定义的Surface对象表示所有载入的图像，其中get_rect()反法返回一个覆盖图像的矩形Rect对象
        # Rect对象有一些重要的属性，如：top，botton，letf、right表示上下左右
        # width，height表示宽高   我有这些值之后，对于我们编写程序十分方便
        imgRect = img.get_rect()
        # 图片位置
        # 中央x坐标整数值 顶部y坐标的整数值
        imgRect.midtop = 80, 10
        # 将一个图像绘制在一个图像上，及将img绘制在imgRect位置上。通过Rect对象上引导对图片的绘制
        screen.blit(img, imgRect)
        # 监听事件
        # pygame.event.get() 的作用是获取事件列表。事件列表内包含0个或多个事件对象 （点击 鼠标移动 关闭窗口）
        # 依次赋值给 event 变量
        for event in pygame.event.get():
            # 检测到鼠标
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 获取鼠标位置
                mouse_pos = pygame.mouse.get_pos()
                # 若点击了喜欢按钮，停止 while 循环
                if mouse_pos[0] < like_pos_x + like_pos_width and mouse_pos[0] > like_pos_x and mouse_pos[
                    1] < like_pos_y + like_pos_height and mouse_pos[1] > like_pos_y:
                    like_color = bg_color
                running = False
            # 获取鼠标位置
            # 若鼠标位置位于按钮区域内
            # 则随机生成按钮位置进行显示
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < unlike_pos_x + unlike_pos_width and mouse_pos[0] > unlike_pos_x and \
                mouse_pos[1] < unlike_pos_y + unlike_pos_height and mouse_pos[1] > unlike_pos_y:
            while True:
                unlike_pos_x, unlike_pos_y = get_random_pos()
                text = button_text_list[random.randint(0, len(button_text_list) - 1)]
                if mouse_pos[0] < unlike_pos_x + unlike_pos_width and mouse_pos[0] > unlike_pos_x and \
                        mouse_pos[1] < unlike_pos_y + unlike_pos_height and mouse_pos[1] > unlike_pos_y:
                    continue
                break
        title('宝贝，我观察你很久了', screen, scale=[1.8, 10])
        title('做我女朋友好不好呀', screen, scale=[1.8, 3])
        button('好的', like_pos_x, like_pos_y, like_pos_width,
               like_pos_height, like_color, screen)
        button(text, unlike_pos_x, unlike_pos_y, unlike_pos_width,
               unlike_pos_height, (216, 191, 216), screen)
        # 显示游戏
        # 刷新屏幕，以使最近的绘制操作生效。
        pygame.display.flip()
        # 对窗口进行更新
        pygame.display.update()
    # 创建Clock对象，用于操作时间
    # tick(60)控制帧速度，即窗口刷新速度，每秒钟60次帧刷新，视频中每次展示的静态图像称为帧
    pygame.time.Clock().tick(60)
    show_like_interface('我就知道小姐姐你也喜欢我~', screen, color=(0, 0, 0))


# 表示程序的主入口。所以以后为了避免该文件被外部文件调用，一般建议加上
if __name__ == '__main__':
    main()
