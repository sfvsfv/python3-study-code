# 石头剪刀布
import random
player = input("请输入您要出的拳 石头（1）/剪刀（2）/布（3）：")
choice = ['1', '2', '3']
computer = random.sample(choice, 1)
computer_1 = computer[0]
print("玩家选择的拳头是 %s - 电脑出的拳是 %s" % (player, computer_1))
if (player == '1' and computer_1 == '3') or (player == '2' and computer_1 == '3') or (player == '3' and computer_1 == '1'):
    print("电脑弱爆了！")
elif player == computer_1:
    print("心有灵犀！")
else:
    print("不服气，再来！")
