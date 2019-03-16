import unittest
import requests
from homework.homework3_common import select_card_number,del_card_number, get_conn,install_card_number,add_new_card
from homework.homework3_test_data import URL,DataSourceID,MethodId_01A,CardNumber,CardNumber1,CardNumber2,DB_longtengserver
from homework.homework3_test_data import UserName,IdNumber,IdType,UserID,ErrorCardNumber,MethodId_error
from homework.homework3_test_data import BlackCardNumber,RegistCardNumber,CompanyCardNumber


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conn = get_conn(DB_longtengserver)
        result = select_card_number(conn,CardNumber)
        if result:
            del_card_number(conn,CardNumber)
        result = select_card_number(conn,CardNumber1)
        if result:
            del_card_number(conn,CardNumber1)
        result = select_card_number(conn,CardNumber2)
        if result:
            del_card_number(conn,CardNumber2)
        try:
            add_new_card(CardNumber)
            add_new_card(CardNumber1)
            add_new_card(CardNumber2)
        except Exception as ex:
            conn.rollback()
        conn.close()
        print("绑定加油卡测试环境准备成功，新建卡号")


    @classmethod
    def tearDownClass(cls):
        conn = get_conn(DB_longtengserver)
        del_card_number(conn,CardNumber)
        del_card_number(conn,CardNumber1)
        del_card_number(conn,CardNumber2)
        conn.close()
        print("绑定加油卡测试环境清理完成，新建卡号删除")


    def test_01_binding_card(self):
        data = {"dataSourceId": DataSourceID,
                "methodId": MethodId_01A,
                "CardUser":
                    {"userName": UserName,
                     "idType": IdType,
                     "idNumber": IdNumber},
                "CardInfo":
                    {"cardNumber": CardNumber}
                }
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(5010, res_dic["code"])
        self.assertEqual("绑定成功", res_dic["msg"])
        self.assertEqual(UserID, res_dic["result"]["UserId"])
        self.assertTrue(True, res_dic["success"])


    def test_02_binding_card_old_card(self):
        data = {"dataSourceId": DataSourceID,
                "methodId": MethodId_01A,
                "CardUser":
                    {"userName": UserName,
                     "idType": IdType,
                     "idNumber": IdNumber},
                "CardInfo":
                    {"cardNumber": CardNumber}
                }
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(5041, res_dic["code"])
        self.assertEqual("卡已经被绑定,无法绑定", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])

    def test_03_binding_2th_card(self):
        data = {"dataSourceId": DataSourceID,
                "methodId": MethodId_01A,
                "CardUser":
                    {"userName": UserName,
                     "idType": IdType,
                     "idNumber": IdNumber},
                "CardInfo":
                    {"cardNumber": CardNumber1}
                }
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(5010, res_dic["code"])
        self.assertEqual("绑定成功", res_dic["msg"])
        self.assertEqual(UserID, res_dic["result"]["UserId"])
        self.assertTrue(True, res_dic["success"])


    def test_04_binding_3th_card(self):
        data = {"dataSourceId": DataSourceID,
                "methodId": MethodId_01A,
                "CardUser":
                    {"userName": UserName,
                     "idType": IdType,
                     "idNumber": IdNumber},
                "CardInfo":
                    {"cardNumber": CardNumber2}
                }
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(5014, res_dic["code"])
        self.assertEqual("每个用户只能绑定两张卡", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_05_binding_error_card(self):
        data = {"dataSourceId": DataSourceID,
                "methodId": MethodId_01A,
                "CardUser":
                    {"userName": UserName,
                     "idType": IdType,
                     "idNumber": IdNumber},
                "CardInfo":
                    {"cardNumber": ErrorCardNumber}
        }
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(5013,res_dic["code"])
        self.assertEqual("加油卡号不存在",res_dic["msg"])
        self.assertFalse(False,res_dic["success"])


    def test_06_binding_error_dataSourceId(self):
        data = {
            "dataSourceId": DataSourceID,
            "methodId": MethodId_error,
            "CardUser":
                {"userName": UserName,
                 "idType": IdType,
                 "idNumber": IdNumber},
            "CardInfo":
                {"cardNumber": CardNumber}
        }
        res = requests.post(url=URL,json=data)
        res_dic = res.json()
        self.assertEqual(199,res_dic["code"])
        self.assertEqual("业务ID无效",res_dic["msg"])
        self.assertFalse(False,res_dic["success"])


    def test_07_binding_black_card(self):
        data={
            "dataSourceId": DataSourceID,
            "methodId": MethodId_01A,
            "CardUser":
                {"userName": UserName,
                 "idType": IdType,
                 "idNumber": IdNumber},
            "CardInfo":
                {"cardNumber": BlackCardNumber}
        }
        res = requests.post(url=URL,json=data)
        res_dic =res.json()
        self.assertEqual(5011,res_dic["code"])
        self.assertEqual("卡号是否黑名单,无法绑定",res_dic["msg"])
        self.assertFalse(False,res_dic["success"])


    def test_08_commony_card(self):
        data={
            "dataSourceId": DataSourceID,
            "methodId": MethodId_01A,
            "CardUser":
                {"userName": UserName,
                 "idType": IdType,
                 "idNumber": IdNumber},
            "CardInfo":
                {"cardNumber": CompanyCardNumber}
        }
        res = requests.post(url=URL,json=data)
        res_dic =res.json()
        self.assertEqual(5013,res_dic["code"])
        self.assertEqual("加油卡号不存在",res_dic["msg"])
        self.assertFalse(False,res_dic["success"])


    def test_09_regist_card(self):
        data={
            "dataSourceId": DataSourceID,
            "methodId": MethodId_01A,
            "CardUser":
                {"userName": UserName,
                 "idType": IdType,
                 "idNumber": IdNumber},
            "CardInfo":
                {"cardNumber": RegistCardNumber}
        }
        res = requests.post(url=URL,json=data)
        res_dic =res.json()
        self.assertEqual(5012,res_dic["code"])
        self.assertEqual("卡号已经注销,无法绑定",res_dic["msg"])
        self.assertFalse(False,res_dic["success"])


if __name__ == '__main__':
    unittest.main()
