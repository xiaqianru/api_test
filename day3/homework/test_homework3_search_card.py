import unittest
import requests
from homework.homework3_common import select_card_number,del_card_number, get_conn,add_new_card,binding_card,recharge_card
from homework.homework3_test_data import URL,DataSourceID,MethodId_02A,CardNumber,CardNumber1,CardNumber2,DB_longtengserver
from homework.homework3_test_data import UserName,IdNumber,IdType,UserID,ErrorCardNumber,MethodId_error,DataSourceID_error
from homework.homework3_test_data import BlackCardNumber,RegistCardNumber,CompanyCardNumber,Data_null,UserID_error


class test_search_card(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conn= get_conn(DB_longtengserver)
        result = select_card_number(conn,CardNumber)
        if result:
            del_card_number(conn,CardNumber)
        try:
            add_new_card(CardNumber)
            binding_card(CardNumber)
            recharge_card(CardNumber)
        except Exception as ex:
            conn.rollback()
        conn.close()
        print("查询加油卡测试环境准备完成")


    @classmethod
    def tearDownClass(cls):
        conn= get_conn(DB_longtengserver)
        del_card_number(conn,CardNumber)
        conn.close()
        print("查询加油卡测试环境清理完成")


    def test_01_search_card(self):
        params = {"methodId": MethodId_02A, "userId": UserID, "cardNumber": CardNumber, "dataSourceId": DataSourceID}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("成功返回", res_dic["msg"])
        self.assertEqual(CardNumber,res_dic["result"]["cardNumber"])
        self.assertTrue(True, res_dic["success"])


    def test_02_search_null_card(self):
        params = {"methodId": MethodId_02A, "userId": UserID, "cardNumber": ErrorCardNumber, "dataSourceId": DataSourceID}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(400, res_dic["code"])
        self.assertEqual("无查询信息", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_03_search_null_user(self):
        params = {"methodId": MethodId_02A, "userId": UserID_error, "cardNumber": CardNumber, "dataSourceId": DataSourceID}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(400, res_dic["code"])
        self.assertEqual("无查询信息", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_04_search_null_dataSourceId(self):
        params = {"methodId": MethodId_02A, "userId": UserID, "cardNumber": CardNumber, "dataSourceId": DataSourceID_error}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(100, res_dic["code"])
        self.assertEqual("对不起,您的第三方机构无权限访问该接口", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_05_search_black_card(self):
        params = {"methodId": MethodId_02A, "userId": UserID, "cardNumber": BlackCardNumber, "dataSourceId": DataSourceID}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(400, res_dic["code"])
        self.assertEqual("无查询信息", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_06_search_registration_card(self):
        params = {"methodId": MethodId_02A, "userId": UserID, "cardNumber": RegistCardNumber, "dataSourceId": DataSourceID}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(400, res_dic["code"])
        self.assertEqual("无查询信息", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_07_search_company_card(self):
        params = {"methodId": MethodId_02A, "userId": UserID, "cardNumber": CompanyCardNumber, "dataSourceId": DataSourceID}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(400, res_dic["code"])
        self.assertEqual("无查询信息", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_08_search_recharge_card(self):
        params = {"methodId": MethodId_02A, "userId": UserID, "cardNumber": CardNumber, "dataSourceId": DataSourceID}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("成功返回", res_dic["msg"])
        self.assertEqual(CardNumber,res_dic["result"]["cardNumber"])
        self.assertIn("充值金额",res_dic["result"]["rechargeDetails"][0])
        self.assertTrue(True, res_dic["success"])


    def test_09_search_consumption_card(self):
        params = {"methodId": MethodId_02A, "userId": UserID, "cardNumber": CardNumber, "dataSourceId": DataSourceID}
        res = requests.get(url=URL, params=params)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("成功返回", res_dic["msg"])
        self.assertEqual(CardNumber,res_dic["result"]["cardNumber"])
        self.assertIn("消费金额",res_dic["result"]["consumptionDetails"][0])
        self.assertTrue(True, res_dic["success"])


if __name__ == '__main__':
    unittest.main()
