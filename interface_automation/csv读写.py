import csv
import codecs


# 她强由他强，清风拂山岗 ； 她横由他横，明月照大江
# 读取内容
def read_info():
    route = '/Users/tiansimi/PycharmProjects/self_flask/interface_automation/owner_info.csv'
    f_csv = csv.reader(open(route, 'r+'))
    for i in f_csv:
        print(i)


def writer_info():
    data = [
        ("测试1", '软件测试工程师'),
        ("测试2", '软件测试工程师'),
        ("测试3", '软件测试工程师'),
        ("测试4", '软件测试工程师'),
        ("测试5", '软件测试工程师'),
    ]
    with codecs.open('./222.csv', 'w+') as f:
        f_csv_2 = csv.writer(f)
        for i in data:
            f_csv_2.writerow(i)  # 这里要用writerow不加s


def writer_dict():
    # 直接字典字段写入到CSV文件中
    data = {'id': '123', 'name': 'anjing', 'age': '26'}
    with open('123.csv', 'w')as f:
        fieldnames = {'id', 'name', 'age'}  # 表头
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)


if __name__ == "__main__":
    read_info()
    writer_info()
    writer_dict()
