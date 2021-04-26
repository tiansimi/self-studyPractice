import configparser
import os


class PracticeReadConfig:
    cf = configparser.ConfigParser()
    cf.read('./case.ini', encoding='utf-8')
    sec = cf.sections()
    print(sec)
    opt = cf.options('DB')
    print(opt)
    # items得到section的所有键值对
    value = cf.items('DB')
    print(value)
    print(dict(value))  # 转换成字典
    mysql_host = cf.get('DB', 'db_config')
    print(mysql_host)



