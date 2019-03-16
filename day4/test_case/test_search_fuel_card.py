import unittest
import requests
import xlrd
import json

from lib.excel import Excel


class TestSearchFuelCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.excel = Excel("加油卡完整用例.xls")
        cls.sheet_data = cls.excel.get_data("查询")

    def test_search_exist_fuel_card(self):
        case_data = self.sheet_data["接口、参数正常"]
        url = case_data["接口地址(名称)URL"]
        expect = json.loads(case_data["预期结果"])
        res = requests.get(url=url)
        self.assertEqual("成功返回",res.json()["msg"])



if __name__ == '__main__':
    unittest.main()