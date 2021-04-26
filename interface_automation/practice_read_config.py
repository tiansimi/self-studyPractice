import configparser
import os
from interface_automation.tools import project_path


class PracticeReadConfig:
    cf = configparser.ConfigParser()
    path = os.path.join(project_path.path, 'conf', 'case.ini')
    cf.read(path, encoding='utf-8')
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



