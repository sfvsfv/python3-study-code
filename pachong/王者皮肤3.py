import requests
import json
import pprint
url='http://pvp.qq.com/web201605/js/herolist.json'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
}
response=requests.get(url=url,headers=headers)

list=response.json()
pprint.pprint(list)
