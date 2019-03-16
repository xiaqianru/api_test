import unittest
import requests
from lib.db import get_conn
from common import get_user_data,del_user

NEW_USER = "王一二"
EXIST_USER = "张三"

# 1.编写一个测试类，以Test开头，继承unittest.TestCase
class TestReg(unittest.TestCase):
    @classmethod    # 初始化
    def setUpClass(cls):
        cls.conn = get_conn()
        cls.url = "http://115.28.108.130:5000/api/user/reg/"

    # 编写具体的测试用例方法，以test_开头
    def test_reg_normal(self):
        # 环境变量检查及数据准备
        conn = get_conn()
        result = get_user_data(conn,NEW_USER)
        if result:
            del_user(conn,NEW_USER)
        # 3.组装和发送请求
        url = "http://115.28.108.130:5000/api/user/reg/"
        data = {"name": NEW_USER,"password": "123456"}
        res = requests.post(url=url,json=data)
        res_dict = res.json()
        # 断言
        self.assertEqual("100000",res_dict["code"])
        self.assertEqual("成功",res_dict["msg"])
        self.assertEqual(NEW_USER,res_dict["data"]["name"])

        result2 = get_user_data(conn,NEW_USER)
        print(result2)
        name = result2[0][1]
        self.assertEqual(NEW_USER, name)

        #环境清理
        del_user(conn,NEW_USER)
        conn.close()


if __name__ == "__main__":
    pass
