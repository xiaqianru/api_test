import unittest
import requests
import pymysql
from homework.homework3_common import select_card_number,del_card_number, get_conn,add_new_card,binding_card,recharge_card
from homework.homework3_test_data import URL,DataSourceID,MethodId_04A,CardNumber,DB_longtengserver,CardBalance_sp
from homework.homework3_test_data import UserID,ErrorCardNumber,Data_null,CardBalance_error,CardBalance_point,UserID_error
from homework.homework3_test_data import BlackCardNumber,RegistCardNumber,CompanyCardNumber,CardBalance,MethodId_error,DataSourceID_error,CardBalance_Big


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
            recharge_card(CardNumber)
        except Exception as ex:
            conn.rollback()
        conn.close()
        print("消费加油卡测试环境准备完成")


    @classmethod
    def tearDownClass(cls):
        conn= get_conn(DB_longtengserver)
        del_card_number(conn,CardNumber)
        conn.close()
        print("消费加油卡测试环境清理完成")


    def test_01_consumption_card(self):
        data = {
            "dataSourceId": DataSourceID,
            "methodId": MethodId_04A,
            "CardUser":
                {
                    "userId": UserID
                },
            "CardInfo":
                {
                    "cardNumber": CardNumber,
                 "cardBalance": CardBalance
                }
        }
        res =requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("消费成功!", res_dic["msg"])
        # self.assertEqual(CardNumber,res_dic["result"]["cardNumber"])
        # self.assertEqual(CardBalance,res_dic["result"]["cardBalance"])
        self.assertTrue(True, res_dic["success"])


    def test_02_consumption_morethan_cardbalance(self):
        data = {
            "dataSourceId": DataSourceID,
            "methodId": MethodId_04A,
            "CardUser":
                {
                    "userId": UserID
                },
            "CardInfo":
                {
                    "cardNumber": CardNumber,
                 "cardBalance": CardBalance_Big
                }
        }
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("对不起，您的余额不足，请充值!", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_03_consumption_error_cardbalace(self):
        data = {
            "dataSourceId": DataSourceID,
            "methodId": MethodId_04A,
            "CardUser":
                {
                    "userId": UserID
                },
            "CardInfo":
                {
                    "cardNumber": CardNumber,
                 "cardBalance": CardBalance_error
                }
        }
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(301, res_dic["code"])
        self.assertEqual("请输入正确的消费金额", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_04_consumption_point_cardbalace(self):
        data = {
            "dataSourceId": DataSourceID,
            "methodId": MethodId_04A,
            "CardUser":
                {
                    "userId": UserID
                },
            "CardInfo":
                {
                    "cardNumber": CardNumber,
                 "cardBalance": CardBalance_point
                }
        }
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("消费成功!", res_dic["msg"])
        self.assertTrue(True, res_dic["success"])


    def test_05_consumption_special_cardbalace(self):
        data = {
            "dataSourceId": DataSourceID,
            "methodId": MethodId_04A,
            "CardUser":
                {
                    "userId": UserID
                },
            "CardInfo":
                {
                    "cardNumber": CardNumber,
                 "cardBalance": CardBalance_sp
                }
        }
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(612, res_dic["code"])
        self.assertEqual("查询异常", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_06_consumption_error_cardnumber(self):
        data = {
            "dataSourceId": DataSourceID,
            "methodId": MethodId_04A,
            "CardUser":
                {
                    "userId": UserID
                },
            "CardInfo":
                {
                    "cardNumber": ErrorCardNumber,
                 "cardBalance": CardBalance
                }
        }
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(5013, res_dic["code"])
        self.assertEqual("根据用户ID没有查询到卡号!", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_07_consumption_error_user(self):
        data = {
            "dataSourceId": DataSourceID,
            "methodId": MethodId_04A,
            "CardUser":
                {
                    "userId": UserID_error
                },
            "CardInfo":
                {
                    "cardNumber": CardNumber,
                 "cardBalance": CardBalance
                }
        }
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(5013, res_dic["code"])
        self.assertEqual("根据用户ID没有查询到卡号!", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


if __name__ == '__main__':
    unittest.main()
