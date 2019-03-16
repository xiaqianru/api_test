import unittest
import requests
import pymysql
from homework.homework3_common import select_card_number,del_card_number, get_conn,add_new_card,binding_card
from homework.homework3_test_data import URL,DataSourceID,MethodId_01A,MethodID_03A,CardNumber,CardNumber1,CardNumber2,DB_longtengserver
from homework.homework3_test_data import UserName,IdNumber,IdType,UserID,ErrorCardNumber,MethodId_error,Data_null,CardBalance_error
from homework.homework3_test_data import BlackCardNumber,RegistCardNumber,CompanyCardNumber,CardBalance,MethodId_error,DataSourceID_error


class test_recharge_card(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conn= get_conn(DB_longtengserver)
        result = select_card_number(conn,CardNumber)
        if result:
            del_card_number(conn,CardNumber)
        try:
            add_new_card(CardNumber)
            binding_card(CardNumber)
        except Exception as ex:
            conn.rollback()
        conn.close()
        print("充值加油卡测试环境准备完成")


    @classmethod
    def tearDownClass(cls):
        conn= get_conn(DB_longtengserver)
        del_card_number(conn,CardNumber)
        conn.close()
        print("充值加油卡测试环境清理完成")


    def test_01_recharge_card(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": CardNumber, "cardBalance": CardBalance}}
        res =requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("充值成功", res_dic["msg"])
        self.assertEqual(CardNumber,res_dic["result"]["cardNumber"])
        self.assertEqual(CardBalance,res_dic["result"]["cardBalance"])
        self.assertTrue(True, res_dic["success"])


    def test_02_recharge_null_methodId(self):
        data = {"dataSourceId": DataSourceID, "methodId": Data_null, "CardInfo": {"cardNumber": CardNumber, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(301, res_dic["code"])
        self.assertEqual("业务ID不能为空!", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_03_recharge_null_dataSourceId(self):
        data = {"dataSourceId": Data_null, "methodId": MethodID_03A, "CardInfo": {"cardNumber": CardNumber, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(301, res_dic["code"])
        self.assertEqual("第三方平台ID不能为空!", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_04_recharge_null_card(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": Data_null, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(301, res_dic["code"])
        self.assertEqual("卡号不能为空!", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_05_recharge_null_cardBalance(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": CardNumber, "cardBalance": Data_null}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(300, res_dic["code"])
        self.assertEqual("金额不能为空", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_06_recharge_error_methodId(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodId_error, "CardInfo": {"cardNumber": CardNumber, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(199, res_dic["code"])
        self.assertEqual("业务ID无效", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_07_recharge_error_dataSourceId(self):
        data = {"dataSourceId": DataSourceID_error, "methodId": MethodID_03A, "CardInfo": {"cardNumber": CardNumber, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(100, res_dic["code"])
        self.assertEqual("对不起,您的第三方机构无权限访问该接口", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_08_recharge_error_cardnumber(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": ErrorCardNumber, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(5013, res_dic["code"])
        self.assertEqual("加油卡号不存在", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_09_recharge_error_cardBalance(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": CardNumber, "cardBalance": CardBalance_error}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(300, res_dic["code"])
        self.assertEqual("金额需为整数", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_10_recharge_black_card(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": BlackCardNumber, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(5011, res_dic["code"])
        self.assertEqual("卡号是否黑名单,无法充值", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_11_recharge_registration_card(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": RegistCardNumber, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(5012, res_dic["code"])
        self.assertEqual("卡号已经注销,无法充值", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_12_recharge_company_card(self):
        data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": CompanyCardNumber, "cardBalance": CardBalance}}
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(5013, res_dic["code"])
        self.assertEqual("加油卡号不存在", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


if __name__ == '__main__':
    unittest.main()
