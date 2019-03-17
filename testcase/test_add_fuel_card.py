import unittest
import logging
import requests
import ddt
from lib.excel import Excel
from lib.db import DB
from lib.utils import json2dict

excel = Excel("data.xls")  # 调用Excel的类，
case_list = excel.get_sheet_data("添加加油卡")  # 获取“添加加油卡”表的数据，直接调用get_sheet_data

@ddt.ddt   # 装饰器
class TestAddFuelCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DB()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    @ddt.data(*case_list)   # 字典拆包用两个*，列表拆包用一个*
    def test_add_fuel_card(self,case_data):
        # case_data = self.case_list[0]   # 整张表取第一条数据
        case_id, tile = case_data[0], case_data[1]  # 取数据表中第0.1列数据（从0开始计数）
        logging.info("执行第{}条用LI：{}".format(case_id, tile))

        method, url, headers, data = case_data[2], case_data[3], json2dict(case_data[4]), json2dict(case_data[5])  # 取数据表中第2,3,7列数据（从0开始计数）
        logging.info("请求方法：{}，url：{}，请求头：{}，请求体：{}".format(method, url, headers, data))

        setup_sql = case_data[6]
        if setup_sql:
            self.db.execute(setup_sql)

        res = requests.request(method, url, headers=headers,json=data)
        expect = json2dict(case_data[7])
        self.assertEqual(expect, res.json())


if __name__ == '__main__':
    unittest.main()
