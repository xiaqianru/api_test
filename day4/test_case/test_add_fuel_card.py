import unittest
import requests
import unittest
import json
import logging

from test_case.basecase import BaseCase

class TestAddFuelCard(BaseCase):

    def test_add_fuel_card(self):
        self.get_case_data("添加加油卡","接口、参数正确")
        card_number = json.loads(self.case_data["入参"])["CardInfo"]["cardNumber"]
        self.db.del_card_if_exist(card_number)
        self.run_case()
        self.assertTrue(self.db.is_card_exist(card_number))
        self.db.del_card_if_exist(card_number)

    def test_add_exist_fuel_card(self):
        self.get_case_data("添加加油卡", "参数相同，重复添加")
        self.run_case()

    def test_add_tow_fuel_card(self):
        self.get_case_data("添加加油卡", "同一账号添加第2个加油卡")
        card_number = json.loads(self.case_data["入参"])["CardInfo"]["cardNumber"]
        self.db.del_card_if_exist(card_number)
        self.run_case()
        self.assertTrue(self.db.is_card_exist(card_number))
        self.db.del_card_if_exist(card_number)

    def test_add_3th_fuel_card(self):
        self.get_case_data("添加加油卡", "同一账号添加第3个加油卡")
        self.run_case()

    def test_error_data(self):
        self.get_case_data("添加加油卡", "入参格式错误")
        self.run_case()

if __name__ == '__main__':
    unittest.main()
