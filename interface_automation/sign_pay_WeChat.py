'''
接口名称：微信支付
实现目标：微信支付sign签名md5加密
签名算法规则：
1、参数名ASCII码从小到大排序（字典序）
2、如果参数的值为空不参与签名，
3、参数名区分大小写
4、验证调用返回或者微信主动通过签名时，传送的sign参数不参与签名，将生产的签名与该sing值做校验
5、微信接口可能增加字段，验证签名时，必须支持增加的扩展字段
'''

# 导入数据处理加密的包
import hashlib

keyString = "192006250b4c09247ec02edce69f6a2d"
# 将所有发送的数据或者接受的数据定义为字典类型
data = {
    'appid': 'wxd930ea5d5a258f4f',
    'mch_id': '10000100',
    'device_info': '1000',
    'body': 'test',
    'nonce_str': 'ibuaiVcKdpRxkhJA',
    'string1': '',
    'string2': '',
    'sign': 'fdsfdhgjghjf'
}


# 定义函数作用：去电参数值为空或者参数名为sign的数据，返回参与签名的字典数据类型
def GetSignData(data):
    signData = {}
    for key, value in data.items():
        if key != 'sign' and value != '':
            signData[key] = value
    return signData


# 对参数按照key = value的格式，并按照ASCII码从小到大排序，拼接成字符串stringA，最后拼接上key，返回拼接api秘钥
def SignString(signData, key):
    list = []
    stringA = ''
    # 循环遍历字典数据的键值，取出放入列表中
    for i in signData.keys():
        list.append(i)
    # 对列表的对象进行排序，默认升序，即按照ASCII码从小到大排序
    list.sort()
    for i in list:
        stringA += i + '=' + signData[i] + '&'
    stringA += 'key' + '=' + key
    return stringA


signData = GetSignData(data)
# 获取需要加密的字符串
signBody = SignString(signData, keyString)
# 创建对象md
md = hashlib.md5()
# d对字符串进行编码
md.update(signBody.encode('utf-8'))
# 数据加密
signValue = md.hexdigest()
signValue = signValue.upper()
print(signValue)

