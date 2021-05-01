import json
data=[{
"name":"chuan",
"age":"20",
"interest":"game"
}]
with open('result.json','w',encoding='utf-8') as f:
    f.write(json.dumps(data))#dumps把json转为字符串，写入文件
    f.write(json.dumps(data,indent=2))#保留json个数，加个缩进字符为2即可
