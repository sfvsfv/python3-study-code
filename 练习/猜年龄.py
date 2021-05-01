import random
print("猜年龄小游戏")
age=int(input("输入你猜测的年龄："))
a=1
b=1
while a>=0:
    computer=random.randint(0,101)
    if age==computer:
        print('恭喜猜对了，你真聪明！')
        break
    else:
        a+=1
        print('你已经猜错了%d次，最多猜三次哦，再来！'%(a-1))
        n=input()
        if n=='y':
            answer=str(input('请输入你猜测的年龄：'))
        if n=='n':
            break
    if a%3==0:
        a = 1
        b = b + 1
        print("你已经猜错三次，是否继续游戏，是则输入Y，开始第%d轮猜测游戏，否则输入N"%b)
        anewer=str(input(""))
        if anewer=='Y':
            print('最多只能猜三次，游戏重新开始了哦')
            n=int(input('请输入你猜测的年龄：'))
            if n==computer:
                print("猜对了哦")
            else:
                a=a+1
                print('你已经猜错了%d次，再来！记住最多猜三次哦'%(a-1))
                n=int(input('请输入你的年龄：'))
        if anewer=="N":
            break
