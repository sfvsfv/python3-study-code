def bonus(time):
    if time < 6:
        money = 500
        return money
    elif 6 <= time <= 12:
        money = 120 * time
        return money
    elif time > 12:
        money = 180 * time
        return money
def info():
     name = str(input('输入姓名'))
     time=int(input("输入时间："))
     money=bonus(time)
     print('%s来了%s，获得了%s奖金'%(name, time,money))
info()
