# 接口自动拉取房间信息后，存入csv中,用的pytest
import pytest
import json
import requests
import csv
from collections import OrderedDict


class Test_search_hourse():
    def setup(self):  # 每个用例开始前执行
        url = "http://117.158.24.187:8008/kangbao/getArchive"
        headers = {
            "Content-Type": "application/json",
            "appId": "e10adc3949ba59abbe56e057f20f883e",
            "appSecret": "e10adc3949ba59abbe56e057f20f883e"
        }
        payload = {
            "mobile": "17310520712"
        }  # payload参数是字典类型
        data_json = json.dumps(payload)
        self.r = requests.post(url=url, headers=headers, data=data_json, verify=False)

    def test_searchInfo(self):
        try:
            x = self.r.json()
            print(x)
            y = x['result']
        except:
            print("该用户没有房间！")

        for i in y:
            print("楼栋号：%s,\n房间号：%s,\n业主：%s" % (i['buildingChn'], i['houseChn'], i['userChn']))

    def test_save(self):
        rows = []
        try:
            a = self.r.json()
            b = a['result']
        except:
            print("该用户没有房间！")
        for i in b:
            print("要取的：\n%s" % i)
            row_info = {}
            for key in i:
                # print("打印遍历的键：%s"%key)
                if key == 'buildingChn':
                    row_info['buildingChn'] = i['buildingChn']  # 将取出的键值对存入字典中
                elif key == 'houseChn':
                    row_info['houseChn'] = i['houseChn']
                elif key == 'userChn':
                    row_info['userChn'] = i['userChn']
            rows.append(row_info)  # 将筛选出的字典以元素形式存入列表

            # rows.append(i['buildingChn'])
        headers = ['buildingChn', 'houseChn', 'userChn']
        # rows =[]
        print("添加字典后的列表：%s" % rows)
        with open("./owner_info.csv", "w+") as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(rows)


if __name__ == "__main__":
    pytest.main(['-s', 'test_search_hourse.py'])
