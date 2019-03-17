'''数据库操作'''
import pymysql
import logging
from config import db_config

class DB(object):
    def __init__(self):    # 建立数据库连接
        self.conn = pymysql.connect(**db_config, autocommit=True)
        self.cur = self.conn.cursor()

    def execute(self,sql):   # 执行数据库语句
        logging.debug("执行sql：{}",format(sql))
        try:
            self.cur.execute(sql)
        except pymysql.err.ProgrammingError as ex:    # 捕获出错信息，打印错误信息
            logging.error("sql语法错误：sql- {}  错误信息- {}",format(sql,ex))
        except pymysql.err.IntegrityError as ex:
            logging.error("sql执行错误：sql- {}  错误信息- {}",format(sql,ex))
        else:
            result = self.cur.fetchall()    # 查询语句返回信息，执行语句返回空
            logging.debug("sql执行数据结果：{}".format(result))

    def close(self):   # 关闭数据库
        self.cur.close()
        self.conn.close()




