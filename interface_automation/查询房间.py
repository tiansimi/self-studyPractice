# 08正式  07测试
import requests
import json
import csv
url = "http://117.158.24.187:8008/kangbao/getArchiveHouseInfo"
headers = {
    "Content-Type": "application/json",
    "appId": "e10adc3949ba59abbe56e057f20f883e",
    "appSecret": "e10adc3949ba59abbe56e057f20f883e"
}
payload = {
    "mobile": "17310520712"
}  # payload参数是字典类型
data_json = json.dumps(payload)
r = requests.post(url=url, headers=headers, data=data_json, verify=False)
x = r.json()
print(x)
print(type(x))
#print(x.items())  # dict.items()会返回一个由元组组成的列表
#print(x['result'][0])
try:
    y = x['result'][0]
except:
    print("该用户没有房间！")
d = x['result']
print(d)

for i in d:
    print("楼栋号：%s,\n房间号：%s,\n业主：%s" % (i['buildingChn'], i['houseChn'], i['userChn']))

