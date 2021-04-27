import mysql.connector
from interface_automation import read_config


class DoMysql:

    def do_mysql(self, query_sql):
        db_config = eval(read_config.Read_config().get_config('DB', 'db_config'))
        # 连接数据库
        cnn = mysql.connector.connect(**db_config)
        # 定义游标
        cursor = cnn.cursor()
        # query_sql = " SELECT employee_id FROM tb_admin WHERE mobile = '15176718391' and type = 1 AND platform = 2"
        # 查询
        cursor.execute(query_sql)
        # 查询一个结果 返回一个元祖
        # res = cursor.fetchone()
        # 查询多个 返回一个列表
        res_all = cursor.fetchall()
        print(res_all)
        cursor.close()
        cnn.close()
        return res_all



