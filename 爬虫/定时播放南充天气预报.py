# import requests
# from lxml import etree
# import pyttsx3
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
# }
# url='https://www.tianqi.com/shanghai/'
# request=requests.get(url=url,headers=headers)
# # print(request.text)
# data=etree.HTML(request.text)
# # print(data)
# list = data.xpath('//dl[@class="weather_info"]//text()')
# # print(list)
# text=''.join(list)
# # print(text)
# weather=pyttsx3.init()
# weather.say(text)
# weather.runAndWait()
#设置每天定时任务播放
import schedule
import time
c=input('地点')
def job():
    print("I'm working...")
    import requests
    from lxml import etree
    import pyttsx3
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    }
    url = 'https://www.tianqi.com/+%s/'%c
    request = requests.get(url=url, headers=headers)
    # print(request.text)
    data = etree.HTML(request.text)
    # print(data)
    list = data.xpath('//dl[@class="weather_info"]//text()')
    # print(list)
    text = ''.join(list)
    print(text)
    weather = pyttsx3.init()
    weather.say(text)
    weather.runAndWait()
job()
# schedule.every(10).seconds.do(job) # 每10秒执行一次
# schedule.every(10).minutes.do(job) # 每10分钟执行一次
# schedule.every().hour.do(job) # 每小时执行一次
# schedule.every().day.at("10:30").do(job) # 每天十点半执行
# schedule.every(5).to(10).minutes.do(job) # 不理解
# schedule.every().monday.do(job) # 每周一执行
# schedule.every().wednesday.at("13:15").do(job) # 每周三13点15执行
# schedule.every().minute.at(":17").do(job) # 不理解
