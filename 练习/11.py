import requests,re
import json
# url = 'https://api.66mz8.com/api/weather.php?location=上海'
# resp = requests.get(url, timeout=5)
# print(resp.json())
# dat=resp.json()
# c=dat['data']
# print(len(c))
# for city, day, week, wendu, weather, wind, pic, tu in data:
# for i in range(len(data.get('data'))):
#     city = data.get('citynm')
#     # city = data.get('citynm')
#     day = data['data'][i]['days']
#     week = data['data'][i]['week']
#     wendu = data['data'][i]['temperature']
#     weather = data['data'][i]['weather']
#     wind = data['data'][i]['wind']
#     pic = data['data'][i]['weather_icon']
#     tu = f"[CQ:image,file={pic}]"
#     print(city, day, week, wendu, weather, wind, tu)
# url = 'http://api.wpbom.com/api/secon.php'
# resp = requests.get(url)
# tu = f"[CQ:image,file={resp}]"
# print(tu)


# url = 'http://api.yanxi520.cn/api/txss.php?msg=从你的全世界路过'
# resp = requests.get(url).text
# print(resp)
# bo=re.findall('图片:(.*)地址',resp)[0]
# print(bo)
