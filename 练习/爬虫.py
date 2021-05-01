#爬取关键词,保存到文件夹
# import urllib.request
#
# url="https://www.baidu.com/s?wd="
#
# key="张杰"
# key_code=urllib.request.quote(key)
# url_all=url+key_code
#
# response=urllib.request.Request(url_all)
#
# data=urllib.request.urlopen(response).read()
# fal=open("C:\Program Files\Intel\Intel(R) Chipset Device Software.text","wb")
# fal.write(data)
# fal.close()

#正则
# import  re
# word="\w\d52python\w"
# string="d152python_d"
# result=re.search(word,string)
# print(result)

# import re
# key=".python.."
# string="gfiaelpythonfwef"
# result=re.match(key,string)
# result2=re.search(key,string).span()
# print(result)
# print(result2)

# import re
# string="ghpythondwdpythonwfpython."
# word=".python."
# result=re.compile(word).findall(string)
# result2=re.sub(word,"hap",string)
# print(result)
# print(result2)

# https://search.jd.com/Search?keyword=%E9%A3%8E%E8%A1%A3%E7%94%B7&wq=%E9%A3%8E%E8%A1%A3%E7%94%B7&page=1&s=1&click=0
# https://search.jd.com/Search?keyword=%E9%A3%8E%E8%A1%A3%E7%94%B7&wq=%E9%A3%8E%E8%A1%A3%E7%94%B7&page=3&s=51&click=0
# https://search.jd.com/Search?keyword=%E9%A3%8E%E8%A1%A3%E7%94%B7&wq=%E9%A3%8E%E8%A1%A3%E7%94%B7&page=5&s=101&click=0
# https://search.jd.com/Search?keyword=%E9%A3%8E%E8%A1%A3%E7%94%B7&wq=%E9%A3%8E%E8%A1%A3%E7%94%B7&page=7&s=151&click=0
