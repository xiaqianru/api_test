import unittest
import requests


class TestLogin2(unittest.TestCase):
    def test_login(self):
        url = "http://115.28.108.130:5000/api/user/login/"
        data = {"name": "张三", "password": "123456"}
        res = requests.post(url=url, data=data)
        self.assertEqual("<h1>登录成功</h1>", res.text)


class TestReg2(unittest.TestCase):
    def test_reg(self):
        url = "http://115.28.108.130:5000/api/user/reg/"
        data = {"name": "张三三三三3", "password": "123456"}
        res = requests.post(url=url, json=data)
        d = res.json()
        # self.assertEqual("100000", d["code"])
        # self.assertEqual("成功", d["msg"])
        # self.assertEqual("张三三三三2", d["data"]["name"])
        e = {"code": "100000",
             "data":
                 {"name": "张三三三三3","password": "e10adc3949ba59abbe56e057f20f883e"},
             "msg": "成功"
             }
        self.assertEqual(e, res.json())

if __name__ == '__main__':
    unittest.main()