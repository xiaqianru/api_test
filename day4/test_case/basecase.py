import unittest
import logging
import requests
import json

from lib.db import DB
from lib.excel import Excel

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DB()
        cls.excel = Excel("加油卡完整用例.xls")

    def get_case_data(self, sheet_name, case_name):
        logging.info("执行用例：{} ：{}----------".format(sheet_name, case_name))
        sheet_data = self.excel.get_data(sheet_name)   # 获取整张表的数据
        self.case_data = sheet_data[case_name]   # 从整张表中获取当前用例标题的用例

    def run_case(self):

        url = self.case_data["接口地址(名称)URL"]       # 从用例数据中获取url，data，expect
        data = json.loads(self.case_data["入参"])
        expect = json.loads(self.case_data["预期结果"])
        logging.info("请求url：{}".format(url))
        logging.info("请求data：{}".format(data))
        logging.info("期望结果：{}".format(expect))

        method = self.case_data["方法"]
        if "GET" == method:
            res = requests.get(url=url)
        else:
            res = requests.post(url=url, json=data)
        logging.info("实际结果：{}".format(res.text))   # 可能不显示中文
        self.assertEqual(expect, res.json())


