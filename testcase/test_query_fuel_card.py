import unittest
import json
import logging
import requests
from lib.excel import Excel
from lib.db import DB
from lib.utils import json2dict


class TestQueryFuelCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DB()
        excel = Excel("data.xls")    # 调用Excel的类，
        cls.case_list = excel.get_sheet_data("查询")   # 获取表查询的数据，直接调用get_sheet_data

    @classmethod
    def tearDownClass(cls):
        cls.db.close()


    def test_query_fuel_card_normal_1(self):
        case_data = self.case_list[0]   # 整张表取第一条数据
        method,url,expect = case_data[2],case_data[3],json2dict(case_data[7])  # 取数据表中第2,3,7列数据（从0开始计数）
        res = requests.request(method,url)
        self.assertEqual(expect,res.json())

    def test_query_fuel_card_normal_2(self):
        case_data = self.case_list[1]   # 整张表取第二条数据
        method,url,expect = case_data[2],case_data[3],json2dict(case_data[7])  # 取数据表中第2,3,7列数据（从0开始计数）
        res = requests.request(method,url)
        self.assertEqual(expect,res.json())


if __name__ == '__main__':
    unittest.main()
