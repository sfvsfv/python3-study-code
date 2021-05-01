import json
data=[{
"name":"川川",
"age":"20",
"interest":"游戏"
}]
with open('result1.json','w',encoding='utf-8') as f:
    f.write(json.dumps(data,indent=2,ensure_ascii=False))#json如果有中文，再加上ensure_ascii=False
