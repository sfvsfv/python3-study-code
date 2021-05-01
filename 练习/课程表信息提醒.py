class school_timetable():
    data1={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[1],"jie":[2],"time":['9:45~11:15'],"name":"体育","address":"第一田径场","teacher":"米珊"}
    data2={'week':[1,2,3,4],"day":[1],"jie":[4],"time":['14:00~15:30'],"name":"形势与政策","address":"西阶四","teacher":"孙国强"}
    data3={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[1],"jie":[5,6],"time":['15:45~17:15,17:25~18:10'],"name":"数据结构与算法","address":"实训楼A406","teacher":"李奕"}
    data4={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[1],"jie":[7],"time":['18:40~20:10'],"name":"求职与面试技巧","address":"B西103","teacher":"刘立坤"}
    data5={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[2],"jie":[2,3],"time":['9:45~11:15,11:25~12:10'],"name":"财政学","address":"A405","teacher":"郑思海"}
    data6={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[3],"jie":[1],"time":['8：00~9:30'],"name":"概率论与数理统计","address":"B西506","teacher":"王立斌"}
    data7={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[3],"jie":[2,3],"time":['9:45~11:15,11:25~12:10'],"name":"面向对象程序设计","address":"实训楼B307","teacher":"申晨"}
    data8={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[3],"jie":[5],"time":['15:45~17:10'],"name":"大学英语3","address":"B东208","teacher":"周锁英"}
    data9={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[4],"jie":[1],"time":['8：00~9:30'],"name":"概率论与数理统计","address":"B西506","teacher":"王立斌"}
    data10={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[3],"jie":[2,3],"time":['9:45~11:15,11:25~12:10'],"name":"金融学","address":"B西508","teacher":"孙文娜"}
    data11={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[5],"jie":[1],"time":['8：00~9:30'],"name":"毛泽东思想和中国特色社会主义理论体系概论","address":"B西402","teacher":"黄逸超"}
    data12={'week':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],"day":[5],"jie":[2,3],"time":['9:45~11:15,11:25~12:10'],"name":"宏观经济学","address":"A105","teacher":"郭晓梅"}
    data13={'week':[1,2],"day":[5],"jie":[4],"time":['14:00~15:30'],"name":"专业导论","address":"西阶二","teacher":"刘冲"}
    data14={'week':[1,3,5,7,9,11,13,15,17],"day":[5],"jie":[5],"time":['15:45~17:10'],"name":"大学英语3","address":"C405","teacher":"周锁英"}

import time  #导入时间模块               #前面我们已经储存好了课程信息，下面我的部分是时间的调用。
import datetime #导入日期模块  这两个模块是差不多的
start_school='20200901'    #假设开学时间是2020年九月一号开始

def account_week(date):  #定义函数：计算经过多少周了
    date1 = time.strptime(date,"%Y%m%d") #用time.strptime函数，把时间字符串转换为年月日格式的时间元组
    date2 = datetime.datetime.now().timetuple()#datetime.timetuple()方法用于操作模块datetime的datetime类的对象，用来得到当前时间
    date1 = datetime.datetime(date1[0], date1[1], date1[2])#对上面的date1时间具体划分为：年（用0表示），月（用1表示），日（用2表示）
    date2 = datetime.datetime(date2[0], date2[1], date2[2])#对上面的date2时间具体划分为：年（用0表示），月（用1表示），日（用2表示）
    differ = date2 - date1  #两次返回值的差，就是相差天数
    weekth = differ // datetime.timedelta(days=7) + 1#datetime.timedelta代表两个时间之间的时间差，经历过的周数等于相差天数除以7+1，所以内部参数为7
    return weekth   #返回结果
def account_day():     #定义函数，计算天数
    day = datetime.datetime.now()  #获取当前时间
    day = day.weekday() + 1     #获取到今天是这一周的第几天
    return day                  #返回结果                           #这两个函数可以实现的功能就是：计算出当天是开学第几周的第几天

def text(x,y,*arges):
    out.append('本周是' + str(x) + '周')
    for key in range(len(data)):
        if x in data[key]["week"]:
            if y in data[key]["day"]:
                s = '你今天第' + str(data[key]['jie']) + '节有' + \
                    str(data[key]['name']) + "，上课地点：" + str(data[key]['adress'])
                out.append(s)
                #print('你今天第' + str(data[key]['jie']) + '节有' + str(data[key]['name']) +
                #     "，上课地点：" + str(data[key]['adress']))
    if len(out)<=1:
        out.append("今天没课哦，但是要记得学习啊！")
    return out

import smtplib
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText  # 发送正文只包含简单文本的邮件，引入MIMEText即可

mail_msg=""" 猪猪"""              #调用account_time，引入时间，邮件内容
message = MIMEText(mail_msg, 'html', 'utf-8')  # 邮件正文
message['From'] = Header("猪猪呀",'utf-8')  # 邮件上显示的发件人
message['To'] = Header("小橘子",'utf-8')# 邮件上显示的收件人
subject = '课程信息'   #邮件的题目
message['Subject'] = Header(subject, 'utf-8')
sender = '2835809579@qq.com'          # 发件人和收件人
receiver = '3164168751@qq.com'                       # 所使用的用来发送邮件的SMTP服务器
smtpServer = 'smtp.qq.com'
username = '2835809579@qq.com'
password = 'gqejqiqrgkjadejh'   #授权码获取方法：https://baijiahao.baidu.com/s?id=1552315463915496&wfr=spider&for=pc

try:
    smtp = smtplib.SMTP()  # 创建一个连接
    smtp.connect(smtpServer)  # 连接发送邮件的服务器
    smtp.login(username, password)  # 登录服务器
    smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
    print("邮件发送成功！！！")
    smtp.quit()
except smtplib.SMTPException:
    print("邮件发送失败！！！")
