import pymysql
import logging
from config import DB_CONFIG


class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()


    def query(self,sql):
        logging.debug("查询SQl：{}".format(sql))
        self.cur.execute(sql)
        result = self.cur.fetchall()  # 嵌套元组((1,...,...,),(2,...,...,)
        logging.debug("查询结果：{}".format(result))
        return result

    def execute(self, sql):
        logging.debug("执行SQl：{}".format(sql))
        try:
            self.cur.execute(sql)
        except Exception as ex:
            logging.debug(str(ex))
            self.conn.rollback()   #执行sql有问题就可以回滚一下，保证数据库正确

    def is_card_exist(self,card_number):
        sql = "select cardNumber from cardinfo where cardNumber='{}'".format(card_number)
        result = self.query(sql)   #空返回（），非空：（（），）
        if result:
            logging.debug("该卡存在")
            return True
        else:
            logging.debug("该卡不存在")
            return False
        # return True if result else False

    def del_card_if_exist(self,card_number):
        logging.debug("查询卡：{} 是否存在".format(card_number))
        sql= "delete from cardinfo where cardnumber='{}'".format(card_number)
        if self.is_card_exist(card_number):
            self.cur.execute(sql)
            logging.debug("删除成功")


if __name__ =="__main__":
    db = DB()
    db.is_card_exist("2019030500")
    db.def_card_if_exist("2019030500")
