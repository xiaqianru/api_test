import unittest
import requests
from homework.homework3_common import del_card_number,check_card_or_del,get_conn
from homework.homework3_test_data import URL,DataSourceID,MethodId_00A,CardNumber,CardNumber1,CardNumber2,DB_longtengserver
from homework.homework3_test_data import Data_null


class Test_add_card(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conn = get_conn(DB_longtengserver)
        check_card_or_del(conn,CardNumber)
        check_card_or_del(conn,CardNumber1)
        check_card_or_del(conn,CardNumber2)
        conn.close()
        print("增加加油卡测试环境准备成功")

    @classmethod
    def tearDownClass(cls):
        conn = get_conn(DB_longtengserver)
        del_card_number(conn,CardNumber)
        del_card_number(conn,CardNumber1)
        del_card_number(conn,CardNumber2)
        conn.close()
        print("增加加油卡测试环境清理完成")

    def test_01_add_new_card(self):
        data = {"dataSourceId": DataSourceID,	"methodId": MethodId_00A, "CardInfo": {"cardNumber": CardNumber}}
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("添加卡成功", res_dic["msg"])
        self.assertEqual("success", res_dic["success"])

    def test_02_add_old_card(self):
        data = {"dataSourceId": DataSourceID,	"methodId": MethodId_00A, "CardInfo": {"cardNumber": CardNumber}}
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(5000, res_dic["code"])
        self.assertEqual("该卡已添加", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_03_add_new_card2(self):
        data = {"dataSourceId": DataSourceID,	"methodId": MethodId_00A, "CardInfo": {"cardNumber": CardNumber1}}
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("添加卡成功", res_dic["msg"])
        self.assertEqual("success", res_dic["success"])


    def test_04_add_new_card3(self):
        data = {"dataSourceId": DataSourceID,	"methodId": MethodId_00A, "CardInfo": {"cardNumber": CardNumber2}}
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(200, res_dic["code"])
        self.assertEqual("添加卡成功", res_dic["msg"])
        self.assertEqual("success", res_dic["success"])


    def test_05_add_error_data(self):
        data ={"dataSourceId": DataSourceID,	"methodId": MethodId_00A, "CardInfo":"" , "cardNumber": CardNumber2}
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(301, res_dic["code"])
        self.assertIn("参数类型错误", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_06_null_dataSourceId(self):
        data ={"dataSourceId": Data_null, "methodId": MethodId_00A, "CardInfo": {"cardNumber": CardNumber2}}
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(301, res_dic["code"])
        self.assertIn("第三方平台ID不能为空", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_07_null_cardNumber(self):
        data = {"dataSourceId": DataSourceID,	"methodId": MethodId_00A, "CardInfo": {"cardNumber": Data_null}}
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(301, res_dic["code"])
        self.assertEqual("卡号不能为空", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


    def test_08_null_methodId(self):
        data = {"dataSourceId": DataSourceID,	"methodId": Data_null, "CardInfo": {"cardNumber": CardNumber}}
        res = requests.post(url=URL, json=data)
        res_dic = res.json()
        self.assertEqual(301, res_dic["code"])
        self.assertEqual("业务ID不能为空!", res_dic["msg"])
        self.assertFalse(False, res_dic["success"])


if __name__ == '__main__':
    unittest.main()
