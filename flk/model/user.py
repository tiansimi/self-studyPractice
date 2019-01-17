__author__ = 'lenovo'
import pymysql

config = {
    "host": "101.124.9.171",
    "port": 3306,
    "user": "dev",
    "password": "fjrUWqUp4WVi8PE",
    "db": "db_steward",
    "charset": "utf8mb4",
}
conn = pymysql.connect(**config)
cursor = conn.cursor()
sql = "select * from tb_channel_info"
a = cursor.execute(sql)
conn.commit()
for i in cursor:  # 输出查询数据库中的所有渠道数据
    print(i)