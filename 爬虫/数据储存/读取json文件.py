import json
with open('data.json','r') as f:
    str=f.read()
    data=json.loads(str)
    print(data)